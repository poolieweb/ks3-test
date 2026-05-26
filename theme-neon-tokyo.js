/* =============================================================================
   NEON TOKYO STRIKE — decoration script (companion to theme-neon-tokyo.css)
   ----------------------------------------------------------------------------
   Drop in after the engine script in index.html:

     <script src="theme-neon-tokyo.js" defer></script>

   Adds kanji watermarks and decorative under-text labels as real DOM nodes —
   more reliable than CSS pseudo-elements across browsers, and survives the
   engine's innerHTML re-renders via a MutationObserver.
   ============================================================================= */

(() => {
  'use strict';

  const SUBJECT_KANJI = {
    science:   { big: '科', label: 'SCI', glyph: '◇', sub: '科学区' },
    history:   { big: '史', label: 'HIS', glyph: '◆', sub: '歴史区' },
    geography: { big: '地', label: 'GEO', glyph: '▲', sub: '地理区' },
    computing: { big: '電', label: 'CMP', glyph: '●', sub: '電脳区' },
  };

  const KANJI_FONT = 'sans-serif';  // system default sans-serif ships CJK glyphs everywhere

  // Add kanji watermarks to subject cards on the home screen.
  // Idempotent — won't double-up if called multiple times.
  function decorateSubjectCards() {
    document.querySelectorAll('.subject-card').forEach((card) => {
      const subject = ['science', 'history', 'geography', 'computing'].find((s) => card.classList.contains(s));
      if (!subject) return;
      const data = SUBJECT_KANJI[subject];

      // Giant kanji watermark in the bottom-right
      if (!card.querySelector('.nt-watermark')) {
        const wm = document.createElement('span');
        wm.className = 'nt-watermark';
        wm.textContent = data.big;
        wm.setAttribute('aria-hidden', 'true');
        card.appendChild(wm);
      }

      // Small "◇ SCI · 科学区" prefix above the h3 title
      const h3 = card.querySelector('h3');
      if (h3 && !card.querySelector('.nt-prefix')) {
        const prefix = document.createElement('div');
        prefix.className = 'nt-prefix';
        prefix.textContent = `${data.glyph} ${data.label} · ${data.sub}`;
        prefix.setAttribute('aria-hidden', 'true');
        h3.parentNode.insertBefore(prefix, h3);
      }
    });
  }

  // Add kanji prefix to the logo (top bar).
  function decorateLogo() {
    const logo = document.querySelector('.topbar .logo');
    if (!logo || logo.querySelector('.nt-logo-kanji')) return;
    const k = document.createElement('span');
    k.className = 'nt-logo-kanji';
    k.textContent = 'ベルティ';
    k.setAttribute('aria-hidden', 'true');
    logo.insertBefore(k, logo.firstChild);
  }

  // Add kanji under the H1 of any rendered card ("MISSION" / mission name).
  function decorateHeadings() {
    document.querySelectorAll('.card h1').forEach((h1) => {
      if (h1.nextElementSibling?.classList.contains('nt-h1-kanji')) return;
      const k = document.createElement('div');
      k.className = 'nt-h1-kanji';
      // Pick a sub-text by context — the engine renders different h1 text per screen
      const t = (h1.textContent || '').toLowerCase();
      if (t.includes('mastery'))      k.textContent = 'スキル ツリー';
      else if (t.includes('achievement')) k.textContent = 'トロフィー';
      else if (t.includes('history'))     k.textContent = 'セッション';
      else if (t.includes('boss'))        k.textContent = 'ボス バトル';
      else if (t.includes('big') || t.includes('brilliant')) k.textContent = '大成功 ・ しょうり';
      else if (t.includes('nice') || t.includes('session'))  k.textContent = 'ナイス セッション';
      else if (t.includes('streak'))       k.textContent = 'れんぞく しょうり';
      else if (t.includes('boss defeated')) k.textContent = 'ボス げきは';
      else                                  k.textContent = 'ミッション';
      k.setAttribute('aria-hidden', 'true');
      h1.insertAdjacentElement('afterend', k);
    });
  }

  // Decorate the reward code panel.
  function decorateCodeDisplay() {
    document.querySelectorAll('.code-display').forEach((code) => {
      if (code.previousElementSibling?.classList.contains('nt-code-label')) return;
      const label = document.createElement('div');
      label.className = 'nt-code-label';
      if (code.classList.contains('big'))         label.textContent = '★ BIG TREAT · 大ごほうび';
      else if (code.classList.contains('streak')) label.textContent = '👑 STREAK WIN · れんぞく';
      else if (code.classList.contains('report')) label.textContent = '◷ REPORT · ほうこく';
      else                                         label.textContent = '◆ REWARD CODE · ごほうび';
      label.setAttribute('aria-hidden', 'true');
      code.insertAdjacentElement('beforebegin', label);
    });
  }

  // Decorate boss banner.
  function decorateBossBanner() {
    document.querySelectorAll('.boss-banner').forEach((banner) => {
      if (banner.querySelector('.nt-boss-kanji')) return;
      const k = document.createElement('span');
      k.className = 'nt-boss-kanji';
      k.textContent = '巨';
      k.setAttribute('aria-hidden', 'true');
      banner.appendChild(k);

      const warn = document.createElement('div');
      warn.className = 'nt-boss-warn';
      warn.textContent = '⚠ WARNING ⚠';
      banner.insertBefore(warn, banner.firstChild);
    });
  }

  // Decorate question prompts with a 問 kanji.
  function decorateQuestion() {
    document.querySelectorAll('.question-prompt').forEach((q) => {
      if (q.querySelector('.nt-q-kanji')) return;
      const k = document.createElement('span');
      k.className = 'nt-q-kanji';
      k.textContent = '問';
      k.setAttribute('aria-hidden', 'true');
      q.insertBefore(k, q.firstChild);
    });
  }

  // Decorate option-list responses with attack/hit/miss kanji on state change.
  function decorateOptions() {
    document.querySelectorAll('.option').forEach((opt) => {
      // remove stale state badge if class changed
      const existing = opt.querySelector('.nt-opt-badge');
      const state = opt.classList.contains('correct')
        ? { text: '✓ ヒット', cls: 'good' }
        : opt.classList.contains('incorrect')
        ? { text: '✗ ミス', cls: 'bad' }
        : opt.classList.contains('selected')
        ? { text: '▶ 攻撃', cls: 'sel' }
        : null;
      if (existing) {
        if (!state) existing.remove();
        else if (existing.textContent !== state.text) {
          existing.textContent = state.text;
          existing.className = `nt-opt-badge ${state.cls}`;
        }
      } else if (state) {
        const b = document.createElement('span');
        b.className = `nt-opt-badge ${state.cls}`;
        b.textContent = state.text;
        b.setAttribute('aria-hidden', 'true');
        opt.appendChild(b);
      }
    });
  }

  // Run all decorations.
  function decorate() {
    decorateLogo();
    decorateSubjectCards();
    decorateHeadings();
    decorateCodeDisplay();
    decorateBossBanner();
    decorateQuestion();
    decorateOptions();
  }

  // Observe the app root for innerHTML re-renders and re-decorate.
  function start() {
    decorate();
    const root = document.getElementById('app') || document.body;
    const obs = new MutationObserver(() => {
      // Run synchronously — decorate() is idempotent and cheap.
      decorate();
    });
    obs.observe(root, { childList: true, subtree: true });
    // Belt-and-braces: poll briefly in case the engine's first render
    // happens before this observer is set up, or somewhere the observer
    // misses. Stops once decoration is in place.
    let tries = 0;
    const poll = setInterval(() => {
      decorate();
      tries++;
      if (document.querySelector('.nt-watermark') || tries > 20) clearInterval(poll);
    }, 200);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', start);
  } else {
    start();
  }

  // Expose for debugging
  window.__neonTokyoDecor = { decorate, SUBJECT_KANJI, KANJI_FONT };
})();
