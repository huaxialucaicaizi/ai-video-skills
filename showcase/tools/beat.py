"""Code-synthesized, royalty-free beat for showcase videos (no samples, deterministic).

Usage: python3 beat.py <out.wav> [--bpm 120] [--bars 15] [--drop 11] [--style pluck|chip]
  --drop N   : bar index (0-based) where drums drop out for one bar (a "breath"); -1 = none
  --style    : pluck = marimba-like pluck (line-art / explainer); chip = square-wave chiptune (pixel)
  --sfx      : "14:ding,19:pickup,22.5:clear,24:blip" synthesized game sounds placed on beats
Bar 0–1 is an intro (melody + shaker only); drums enter on bar 2; the last bar ends on a held chord.
Then normalize: ffmpeg -i out.wav -af loudnorm=I=-14:TP=-1.5:LRA=11 -ar 48000 music.m4a
"""
import argparse, wave
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("out"); ap.add_argument("--bpm", type=float, default=120); ap.add_argument("--bars", type=int, default=15)
ap.add_argument("--drop", type=int, default=11); ap.add_argument("--style", default="pluck")
ap.add_argument("--sfx", default="", help="comma list of time:kind, kind in ding|pickup|clear|blip")
a = ap.parse_args()

SR = 44100
spb = 60.0 / a.bpm                      # seconds per beat
bar = 4 * spb
N = int(round(a.bars * bar * SR))
mix = np.zeros(N)
rng = np.random.default_rng(7)

def add(sig, t, gain=1.0):
    i = int(round(t * SR))
    if i >= N: return
    j = min(N, i + len(sig)); mix[i:j] += gain * sig[: j - i]

def env(dur, attack=0.004, decay=0.25):
    t = np.arange(int(dur * SR)) / SR
    return np.minimum(1, t / attack) * np.exp(-t / decay), t

def midi(m): return 440.0 * 2 ** ((m - 69) / 12)

def pluck(m, dur=0.45):
    e, t = env(dur, 0.003, 0.16); f = midi(m)
    if a.style == "chip":
        s = np.sign(np.sin(2 * np.pi * f * t)) * 0.5
    else:   # marimba-ish: fundamental + 4th partial, quick decay on the overtone
        s = np.sin(2 * np.pi * f * t) + 0.35 * np.sin(2 * np.pi * 4 * f * t) * np.exp(-t / 0.04)
    return s * e

def bass(m, dur):
    e, t = env(dur, 0.01, 0.5); f = midi(m)
    s = np.sin(2 * np.pi * f * t) + 0.25 * np.sin(2 * np.pi * 2 * f * t)
    return np.tanh(1.5 * s) * e

def kick():
    e, t = env(0.35, 0.001, 0.12)
    ph = 2 * np.pi * np.cumsum(45 + 110 * np.exp(-t / 0.03)) / SR
    return np.sin(ph) * e

def noise(dur, decay, hp=True):
    e, t = env(dur, 0.001, decay); n = rng.standard_normal(len(t))
    if hp: n = np.diff(n, prepend=0)          # crude high-pass
    return n * e

def clap():
    s = np.zeros(int(0.25 * SR))
    for k, off in enumerate((0, 0.011, 0.022)):
        b = noise(0.2, 0.05 if k == 2 else 0.008); i = int(off * SR); s[i:i + len(b)] += b[: len(s) - i]
    return s

def sq(f, dur, gain=1.0, decay=0.08):
    e, t = env(dur, 0.002, decay); return np.sign(np.sin(2 * np.pi * f * t)) * e * gain

def sfx(kind):
    if kind == "ding":    # block bump: two quick high notes
        return np.concatenate([sq(midi(84), 0.06), sq(midi(91), 0.22, 1, 0.09)])
    if kind == "pickup":  # rising arpeggio
        return np.concatenate([sq(midi(m), 0.045, 1, 0.05) for m in (72, 76, 79, 84)] + [sq(midi(88), 0.15, 1, 0.07)])
    if kind == "clear":   # small fanfare
        return np.concatenate([sq(midi(m), d, 1, 0.12) for m, d in ((72, 0.12), (76, 0.12), (79, 0.12), (84, 0.45))])
    if kind == "blip":
        return sq(midi(96), 0.05, 1, 0.03)
    raise SystemExit("unknown sfx " + kind)

# C – Am – F – G, one chord per bar
prog = [(48, [60, 64, 67, 72]), (45, [57, 60, 64, 69]), (41, [57, 60, 65, 69]), (43, [55, 59, 62, 67])]
arp = [0, 1, 2, 3, 2, 1, 2, 3]               # 8th-note pattern indexes into chord
melody_hi = [None, 76, None, 79, 76, None, 74, None]   # light top line every other bar

for b in range(a.bars):
    t0 = b * bar; root, ch = prog[b % 4]
    last = b == a.bars - 1
    drums = b >= 2 and b != a.drop and not last
    if last:   # held final chord on the downbeat + a soft bell an octave up
        for m in ch: add(pluck(m, 2.0) * 0.8, t0, 0.18)
        add(bass(root, 2.0), t0, 0.5); add(pluck(ch[-1] + 12, 1.5), t0 + 2 * spb, 0.14)
        add(kick(), t0, 0.9)
        continue
    for k, idx in enumerate(arp):
        add(pluck(ch[idx]), t0 + k * spb / 2, 0.20 if b >= 2 else 0.16)
    if b % 2 == 1 and b >= 2:
        for k, m in enumerate(melody_hi):
            if m: add(pluck(m, 0.6), t0 + k * spb / 2, 0.13)
    for k in range(8):                       # shaker on 8ths, accented off-beats
        add(noise(0.06, 0.015), t0 + k * spb / 2, 0.05 if k % 2 else 0.025)
    if b >= 2 and b != a.drop:
        add(bass(root, 2 * spb), t0, 0.45); add(bass(root, 2 * spb), t0 + 2 * spb, 0.4)
    if drums:
        for k in (0, 2): add(kick(), t0 + k * spb, 0.9)
        add(kick(), t0 + 3.5 * spb, 0.5)
        for k in (1, 3): add(clap(), t0 + k * spb, 0.35)
    if b == a.drop:                          # short riser into the next bar
        e, t = env(bar, 0.9 * bar, 9); add(noise(bar, 9) * (t / bar) ** 2, t0, 0.08)

for item in filter(None, a.sfx.split(",")):
    tt, kind = item.split(":"); add(sfx(kind), float(tt), 0.16)

mix /= np.max(np.abs(mix)) + 1e-9
fade = int(0.25 * SR); mix[-fade:] *= np.linspace(1, 0, fade)
pcm = (mix * 0.89 * 32767).astype(np.int16)
with wave.open(a.out, "wb") as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())
print(f"{a.out}: {a.bars} bars @ {a.bpm} BPM = {N / SR:.2f}s, drop bar {a.drop}")
