/* ai-video-skills · line-art helpers (needs kit.js + GSAP). Deterministic: everything is
   driven by the paused timeline; line "boil" seeds depend only on time. */
(function () {
  var L = {};

  // Hidden SVG with the boil filters. Two strengths: #boil for drawings, #boilS for text.
  L.installFilters = function () {
    if (document.getElementById("boil")) return;
    var d = document.createElement("div");
    d.style.cssText = "position:absolute;width:0;height:0;overflow:hidden";
    d.innerHTML =
      '<svg width="0" height="0"><defs>' +
      '<filter id="boil" x="-10%" y="-10%" width="120%" height="120%"><feTurbulence id="boilT" type="fractalNoise" baseFrequency="0.022" numOctaves="2" seed="1"/><feDisplacementMap in="SourceGraphic" scale="6" xChannelSelector="R" yChannelSelector="G"/></filter>' +
      '<filter id="boilS" x="-5%" y="-10%" width="110%" height="120%"><feTurbulence id="boilTS" type="fractalNoise" baseFrequency="0.03" numOctaves="1" seed="1"/><feDisplacementMap in="SourceGraphic" scale="3" xChannelSelector="R" yChannelSelector="G"/></filter>' +
      "</defs></svg>";
    document.body.appendChild(d);
  };

  // Line boil: new noise seed every `step` seconds (0.1 s ≈ "on threes" at 30 fps).
  L.boil = function (tl, total, step) {
    step = step || 0.1;
    var a = document.getElementById("boilT"), b = document.getElementById("boilTS");
    var o = { t: 0 }, last = -1;
    tl.fromTo(o, { t: 0 }, { t: total, duration: total, ease: "none", onUpdate: function () {
      var s = (Math.floor(o.t / step) % 7) + 1;
      if (s === last) return; last = s;
      a.setAttribute("seed", s); b.setAttribute("seed", s + 3);
    } }, 0);
    return tl;
  };

  // The Agent: a small line-art robot. viewBox 0 0 300 370; right hand at (252, 292).
  // cls "w" draws it in white (for accent backgrounds).
  L.robot = function (extra, color) {
    var c = color ? " " + color : "";
    return '<svg class="ink robot ' + (extra || "") + '" viewBox="0 0 300 370">' +
      '<g class="r-all">' +
      '<path class="ln r-ant' + c + '" pathLength="1" d="M150 82 C148 70 153 58 150 44"/>' +
      '<circle class="fl acc r-bulb" cx="150" cy="34" r="13"/>' +
      '<path class="ln r-head' + c + '" pathLength="1" d="M96 84 C130 78 176 79 206 84 C226 88 232 104 230 130 C229 158 228 184 214 196 C182 202 122 203 88 196 C72 186 70 158 71 130 C72 102 76 88 96 84 Z"/>' +
      '<circle class="fl r-eye' + (color === "w" ? " w" : "") + '" cx="122" cy="134" r="11"/>' +
      '<circle class="fl r-eye' + (color === "w" ? " w" : "") + '" cx="180" cy="134" r="11"/>' +
      '<path class="ln r-mouth' + c + '" pathLength="1" d="M126 166 C140 178 162 178 176 165"/>' +
      '<path class="ln r-body' + c + '" pathLength="1" d="M104 212 C134 207 168 207 198 212 C206 240 207 278 199 306 C168 312 134 312 103 306 C95 278 96 240 104 212 Z"/>' +
      '<circle class="ln acc r-chest" pathLength="1" cx="151" cy="256" r="16"/>' +
      '<path class="ln r-arm r-arm-l' + c + '" pathLength="1" d="M102 230 C76 242 56 262 48 292"/>' +
      '<path class="ln r-arm r-arm-r' + c + '" pathLength="1" d="M200 230 C226 242 246 262 252 292"/>' +
      '<circle class="ln r-hand' + c + '" pathLength="1" cx="46" cy="304" r="13"/>' +
      '<circle class="ln r-hand' + c + '" pathLength="1" cx="254" cy="304" r="13"/>' +
      '<path class="ln r-leg' + c + '" pathLength="1" d="M128 312 L124 350 L104 352"/>' +
      '<path class="ln r-leg' + c + '" pathLength="1" d="M174 312 L178 350 L198 352"/>' +
      "</g></svg>";
  };

  // Draw every .ln inside sel in order (staggered), like a pen going around.
  L.drawAll = function (tl, sel, at, dur, stagger) {
    var els = document.querySelectorAll(sel + " .ln");
    tl.fromTo(els, { strokeDashoffset: 1 }, { strokeDashoffset: 0, duration: dur || 0.5, ease: "power2.inOut", stagger: stagger == null ? 0.06 : stagger }, at);
    return tl;
  };
  // Fill dots (eyes, bulbs) appear.
  L.dots = function (tl, sel, at) {
    tl.fromTo(document.querySelectorAll(sel + " .fl"), { scale: 0, transformOrigin: "50% 50%" }, { scale: 1, duration: 0.25, ease: "expo.out", stagger: 0.05 }, at);
    return tl;
  };
  // "Slam": text lands from big to normal on a beat. No bounce, a fast expo settle.
  L.slam = function (tl, sel, at, from) {
    tl.fromTo(sel, { autoAlpha: 0, scale: from || 1.6 }, { autoAlpha: 1, scale: 1, duration: 0.28, ease: "expo.out" }, at);
    return tl;
  };
  // Beat bob: tiny vertical bob on every beat between a and b (spb = seconds per beat).
  L.bob = function (tl, sel, a, b, spb, amp) {
    for (var t = a; t < b - 0.01; t += spb) {
      tl.fromTo(sel, { y: 0 }, { y: -(amp || 10), duration: spb / 2, ease: "sine.out", yoyo: true, repeat: 1, immediateRender: false }, t);
    }
    return tl;
  };

  window.L = L;
})();
