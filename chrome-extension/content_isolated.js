/**
 * Typographic Watermarking - Content Method 1: Manual Copy (ISOLATED World)
 * Handles Ctrl+C / Cmd+C events robustly
 */

const FINGERPRINTS = {
  'chatgpt.com': '\u2009',
  'chat.openai.com': '\u2009',
  'claude.ai': '\u200A',
  'gemini.google.com': '\u2005',
  'poe.com': '\u2004',
  'copilot.microsoft.com': '\u2006',
  'perplexity.ai': '\u2007',
  'www.perplexity.ai': '\u2007',
  'pi.ai': '\u2008',
  'huggingface.co': '\u205F',
  'localhost': '\u2009',
  '127.0.0.1': '\u2009'
};

function getFingerprint() {
  return FINGERPRINTS[window.location.hostname] || FINGERPRINTS['localhost'];
}

function getAIName() {
  const h = window.location.hostname;
  if (h.includes('chatgpt') || h.includes('openai')) return 'ChatGPT';
  if (h.includes('claude')) return 'Claude';
  if (h.includes('gemini')) return 'Gemini';
  if (h.includes('poe')) return 'Poe';
  if (h.includes('copilot')) return 'Copilot';
  if (h.includes('perplexity')) return 'Perplexity';
  if (h.includes('pi')) return 'Pi';
  if (h.includes('huggingface')) return 'HuggingChat';
  return 'AI Model';
}

function injectWatermark(text) {
  const fp = getFingerprint();
  if (!fp || !text) return text;
  return text.replaceAll(' ', fp);
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

// METHOD 1: Copy event listener (ISOLATED WORLD)
document.addEventListener('copy', function(e) {
  const fp = getFingerprint();
  if (!fp) return;

  const sel = window.getSelection();
  if (!sel || !sel.toString().trim()) return;

  const original = sel.toString();
  const watermarked = injectWatermark(original);
  const code = fp.charCodeAt(0).toString(16).toUpperCase().padStart(4, '0');

  e.clipboardData.setData('text/plain', watermarked);
  e.preventDefault();

  console.log(`TW [ISO]: Copy event → ${getAIName()} (U+${code})`);
  showNotification(`Watermark: ${getAIName()} (U+${code})`);
}, true); // Capture phase
