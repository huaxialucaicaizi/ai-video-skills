/* ai-video-skills motion kit helpers. Everything is driven by one paused GSAP timeline,
   so frames are deterministic for HyperFrames rendering. */
(function () {
  var K = {};

  // Wrap every character of an element in masked spans so it can rise into view.
  K.split = function (el) {
    if (typeof el === "string") el = document.querySelector(el);
    if (!el || el.dataset.split) return el;
    el.dataset.split = "1";
    el.classList.add("split");
    var walk = function (node) {
      Array.prototype.slice.call(node.childNodes).forEach(function (n) {
        if (n.nodeType === 3) {
          var frag = document.createDocumentFragment();
          Array.from(n.textContent).forEach(function (c) {
            if (c === " ") { frag.appendChild(document.createTextNode(" ")); return; }
            var m = document.createElement("span"); m.className = "mask";
            var s = document.createElement("span"); s.className = "ch"; s.textContent = c;
            m.appendChild(s); frag.appendChild(m);
          });
          node.replaceChild(frag, n);
        } else if (n.nodeType === 1 && n.tagName !== "BR") {
          walk(n);
        }
      });
    };
    walk(el);
    return el;
  };

  // Characters rise from below their mask, with a slight overshoot.
  K.riseChars = function (tl, sel, at, opts) {
    opts = opts || {};
    var el = K.split(sel);
    var chars = el.querySelectorAll(".ch");
    tl.fromTo(chars, { yPercent: 105 },
      { yPercent: 0, duration: opts.d || 0.7, ease: opts.ease || "expo.out", stagger: opts.stagger || 0.035 }, at);
    return tl;
  };

  // Generic rise-in for blocks.
  K.rise = function (tl, sel, at, opts) {
    opts = opts || {};
    tl.fromTo(sel, { autoAlpha: 0, y: opts.y || 60, scale: opts.s || 1 },
      { autoAlpha: 1, y: 0, scale: 1, duration: opts.d || 0.6, ease: opts.ease || "power3.out", stagger: opts.stagger || 0 }, at);
    return tl;
  };

  // Pop with spring for cards / icons.
  K.pop = function (tl, sel, at, opts) {
    opts = opts || {};
    tl.fromTo(sel, { autoAlpha: 0, scale: opts.from || 0.92, y: 30 },
      { autoAlpha: 1, scale: 1, y: 0, duration: opts.d || 0.55, ease: opts.ease || "expo.out", stagger: opts.stagger || 0 }, at);
    return tl;
  };

  // Highlighter mark sweeping under a word (uses --mx custom property).
  K.mark = function (tl, sel, at) {
    tl.fromTo(sel, { "--mx": 0 }, { "--mx": 1, duration: 0.5, ease: "power2.inOut" }, at);
    return tl;
  };

  // Scene in / out: blur-scale transitions.
  K.sceneIn = function (tl, sel, at) {
    tl.fromTo(sel, { autoAlpha: 0, scale: 1.08, filter: "blur(18px)" },
      { autoAlpha: 1, scale: 1, filter: "blur(0px)", duration: 0.55, ease: "power3.out" }, at);
    return tl;
  };
  K.sceneOut = function (tl, sel, at) {
    tl.to(sel, { autoAlpha: 0, scale: 0.94, filter: "blur(14px)", duration: 0.45, ease: "power2.in" }, at);
    return tl;
  };
  // Slow camera push across a scene's life.
  K.push = function (tl, sel, at, dur, amount) {
    tl.fromTo(sel, { scale: 1 }, { scale: 1 + (amount || 0.04), duration: dur, ease: "none" }, at);
    return tl;
  };

  // Count a number up (integer) inside an element.
  K.count = function (tl, sel, from, to, at, dur, suffix) {
    var el = typeof sel === "string" ? document.querySelector(sel) : sel;
    var o = { v: from };
    tl.fromTo(o, { v: from }, {
      v: to, duration: dur || 1.2, ease: "power2.out",
      onUpdate: function () { el.textContent = Math.round(o.v).toLocaleString("en-US") + (suffix || ""); }
    }, at);
    return tl;
  };

  // Draw an SVG path/line (needs pathLength="1" on the element).
  K.draw = function (tl, sel, at, dur) {
    tl.fromTo(sel, { strokeDashoffset: 1 }, { strokeDashoffset: 0, duration: dur || 0.8, ease: "power2.inOut" }, at);
    return tl;
  };

  // Background blobs drift for the whole video.
  K.bgDrift = function (tl, total) {
    tl.to(".blob.b1", { x: 160, y: 120, duration: total, ease: "sine.inOut" }, 0);
    tl.to(".blob.b2", { x: -140, y: -200, duration: total, ease: "sine.inOut" }, 0);
    tl.to(".blob.b3", { x: 120, y: -80, duration: total, ease: "sine.inOut" }, 0);
    tl.fromTo(".rail i", { scaleX: 0 }, { scaleX: 1, duration: total, ease: "none" }, 0);
    return tl;
  };

  window.K = K;
})();
