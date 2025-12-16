/**
 * Typographic Watermarking - Content Script v3 (STABLE)
 * Multiple copy interception methods
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
};

function getFingerprint() {
  return FINGERPRINTS[window.location.hostname] || null;
}

function getAIName() {
  const h = window.location.hostname;
  if (h.includes('chatgpt') || h.includes('openai')) return 'ChatGPT';
  if (h.includes('claude')) return 'Claude';
  if (h.includes('gemini')) return 'Gemini';
  if (h.includes('poe')) return 'Poe';
  if (h.includes('copilot')) return 'Copilot';
  if (h.includes('perplexity')) return 'Perplexity';
  if (h.includes('pi.ai')) return 'Pi';
  if (h.includes('huggingface')) return 'HuggingChat';
  return 'AI';
}

function injectWatermark(text) {
  const fp = getFingerprint();
  if (!fp || !text) return text;
  return text.replace(/ /g, fp);
}

function showNotification(msg) {
  const existing = document.getElementById('tw-notification');
  if (existing) existing.remove();

  const n = document.createElement('div');
  n.id = 'tw-notification';
  n.textContent = msg;
  n.style.cssText = `
    position: fixed; bottom: 20px; right: 20px;
    background: #000; color: #fff;
    padding: 12px 20px; font-family: monospace; font-size: 12px;
    border-radius: 4px; z-index: 999999;
    box-shadow: 0 4px 12px rgba(0,0,0,0.3);
    animation: tw-fade 3s forwards;
  `;

  if (!document.getElementById('tw-styles')) {
    const s = document.createElement('style');
    s.id = 'tw-styles';
    s.textContent = `@keyframes tw-fade { 0%{opacity:0;transform:translateY(10px)} 10%{opacity:1;transform:translateY(0)} 80%{opacity:1} 100%{opacity:0} }`;
    document.head.appendChild(s);
  }

  document.body.appendChild(n);
  setTimeout(() => n.remove(), 3000);
}

// Store original clipboard methods
const originalWriteText = navigator.clipboard.writeText.bind(navigator.clipboard);
const originalWrite = navigator.clipboard.write.bind(navigator.clipboard);

// METHOD 1: Copy event
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

  console.log(`TW: Copy → ${getAIName()} (U+${code})`);
  showNotification(`Watermark: ${getAIName()} (U+${code})`);
}, true);

// METHOD 2: Override Clipboard.writeText
navigator.clipboard.writeText = async function(text) {
  const fp = getFingerprint();
  if (fp && text) {
    const watermarked = injectWatermark(text);
    const code = fp.charCodeAt(0).toString(16).toUpperCase().padStart(4, '0');
    console.log(`TW: writeText → ${getAIName()} (U+${code})`);
    showNotification(`Watermark: ${getAIName()} (U+${code})`);
    return originalWriteText(watermarked);
  }
  return originalWriteText(text);
};

// METHOD 3: Override Clipboard.write
navigator.clipboard.write = async function(items) {
  const fp = getFingerprint();
  if (!fp) return originalWrite(items);

  try {
    const newItems = await Promise.all(items.map(async (item) => {
      const blobs = {};
      for (const type of item.types) {
        const blob = await item.getType(type);
        if (type === 'text/plain') {
          const text = await blob.text();
          const watermarked = injectWatermark(text);
          blobs[type] = new Blob([watermarked], { type });
          const code = fp.charCodeAt(0).toString(16).toUpperCase().padStart(4, '0');
          console.log(`TW: write() → ${getAIName()} (U+${code})`);
          showNotification(`Watermark: ${getAIName()} (U+${code})`);
        } else {
          blobs[type] = blob;
        }
      }
      return new ClipboardItem(blobs);
    }));
    return originalWrite(newItems);
  } catch (err) {
    return originalWrite(items);
  }
};

// Log activation
const fp = getFingerprint();
if (fp) {
  const code = fp.charCodeAt(0).toString(16).toUpperCase().padStart(4, '0');
  console.log(`Typographic Watermark v3 ACTIVE on ${getAIName()} (U+${code})`);
}
