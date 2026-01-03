/**
 * Typographic Watermarking - Content Method 1: Manual Copy (ISOLATED World)
 * Handles Ctrl+C / Cmd+C events robustly
 */

// Domain mapping: substring/suffix -> fingerprint
const FINGERPRINTS = {
  'chatgpt': '\u2009',
  'openai': '\u2009',
  'claude': '\u200A',
  'gemini': '\u2005',
  'googleusercontent': '\u2005', // Gemini sandboxes
  'copilot': '\u2006',
  'perplexity': '\u2007',
  'localhost': '\u2009',
  '127.0.0.1': '\u2009'
};

function getFingerprint() {
  const h = window.location.hostname;
  for (const [key, val] of Object.entries(FINGERPRINTS)) {
    if (h.includes(key)) return val;
  }
  return FINGERPRINTS['localhost'];
}

function getAIName() {
  const h = window.location.hostname;
  if (h.includes('chatgpt') || h.includes('openai')) return 'ChatGPT';
  if (h.includes('claude')) return 'Claude';
  if (h.includes('gemini') || h.includes('googleusercontent')) return 'Gemini';
  if (h.includes('copilot')) return 'Copilot';
  if (h.includes('perplexity')) return 'Perplexity';
  return 'AI Model';
}

function injectWatermark(text) {
  const fp = getFingerprint();
  if (!fp || !text) return text;
  // Use Unicode Property Escape to match ALL Separator, Space characters (U+0020, U+00A0, U+200x, etc)
  return text.replace(/\p{Zs}/gu, fp);
}

function showNotification(msg) {
  if (!document.body) {
    document.addEventListener('DOMContentLoaded', () => showNotification(msg));
    return;
  }

  const existing = document.getElementById('tw-notification-iso');
  if (existing) existing.remove();

  const n = document.createElement('div');
  n.id = 'tw-notification-iso';
  n.textContent = msg;
  n.style.cssText = `
    position: fixed; bottom: 20px; right: 20px;
    background: #000; color: #fff;
    padding: 12px 20px; font-family: monospace; font-size: 12px;
    border-radius: 4px; z-index: 999999;
    box-shadow: 0 4px 12px rgba(0,0,0,0.3);
    animation: tw-fade 3s forwards;
    pointer-events: none;
  `;

  if (!document.getElementById('tw-styles-iso')) {
    const s = document.createElement('style');
    s.id = 'tw-styles-iso';
    s.textContent = `@keyframes tw-fade { 0%{opacity:0;transform:translateY(10px)} 10%{opacity:1;transform:translateY(0)} 80%{opacity:1} 100%{opacity:0} }`;
    document.head.appendChild(s);
  }

  document.body.appendChild(n);
  setTimeout(() => n.remove(), 3000);
}

// Helper to pierce Shadow DOM
function getDeepSelection() {
  // First try standard selection
  let sel = window.getSelection();
  if (sel && sel.toString().length > 0) return sel;

  // Try active element's shadow root
  let active = document.activeElement;
  while (active && active.shadowRoot) {
    const shadowSel = active.shadowRoot.getSelection ? active.shadowRoot.getSelection() : null;
    if (shadowSel && shadowSel.toString().length > 0) return shadowSel;
    active = active.shadowRoot.activeElement;
  }
  return null;
}

// METHOD 1: Copy event listener (ISOLATED WORLD)
// Attaching to window with capture:true is the most aggressive way to see the event first.
window.addEventListener('copy', function(e) {
  const sel = getDeepSelection();
  if (!sel) return; // Silent return if no selection found

  const text = sel.toString();
  if (!text.trim()) return;

  const fp = getFingerprint();
  const watermarked = injectWatermark(text);

  // Use setData to override
  e.clipboardData.setData('text/plain', watermarked);
  e.preventDefault();
  e.stopImmediatePropagation(); // CRITICAL: Prevent site from overwriting our dat

  const code = fp.charCodeAt(0).toString(16).toUpperCase().padStart(4, '0');
  console.log(`TW [ISO]: Copy event → ${getAIName()} (U+${code})`);
  showNotification(`Watermark: ${getAIName()} (U+${code})`);
}, true); // Capture phase

console.log('TW [ISO]: Loaded');
