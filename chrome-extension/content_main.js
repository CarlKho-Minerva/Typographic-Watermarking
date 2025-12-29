/**
 * Typographic Watermarking - Content Method 2 & 3: Clipboard Prototype Patch (MAIN World)
 * Aggressively patches Clipboard.prototype to handle "Copy" buttons
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
    // Wait for body, but also log to console immediately
    console.log('[TW Pending Notification]', msg);
    document.addEventListener('DOMContentLoaded', () => showNotification(msg));
    return;
  }

  const existing = document.getElementById('tw-notification-main');
  if (existing) existing.remove();

  const n = document.createElement('div');
  n.id = 'tw-notification-main';
  n.textContent = msg;
  n.style.cssText = `
    position: fixed; bottom: 60px; right: 20px;
    background: #000; color: #fff;
    padding: 12px 20px; font-family: monospace; font-size: 12px;
    border-radius: 4px; z-index: 999999;
    box-shadow: 0 4px 12px rgba(0,0,0,0.3);
    animation: tw-fade 3s forwards;
    pointer-events: none;
  `;

  if (!document.getElementById('tw-styles-main')) {
    const s = document.createElement('style');
    s.id = 'tw-styles-main';
    s.textContent = `@keyframes tw-fade { 0%{opacity:0;transform:translateY(10px)} 10%{opacity:1;transform:translateY(0)} 80%{opacity:1} 100%{opacity:0} }`;
    document.head.appendChild(s);
  }

  document.body.appendChild(n);
  setTimeout(() => n.remove(), 3000);
}

// ----------------------------------------------------------------------
// NUCLEAR OPTION: Patch Clipboard.prototype
// This affects ALL clipboard instances, even those created before this script runs.
// ----------------------------------------------------------------------

try {
  // Graceful degradation if Clipboard API is missing
  if (window.Clipboard && window.Clipboard.prototype) {
    const proto = window.Clipboard.prototype;

    // 1. Patch writeText
    const originalWriteText = proto.writeText;
    proto.writeText = async function(text) {
      const fp = getFingerprint();
      if (fp && text) {
        // Log attempt
        const code = fp.charCodeAt(0).toString(16).toUpperCase().padStart(4, '0');
        console.log(`TW [PROTO]: writeText interception → ${getAIName()} (U+${code})`);

        try {
          const watermarked = injectWatermark(text);
          showNotification(`Watermark: ${getAIName()} (U+${code})`);
          return originalWriteText.call(this, watermarked);
        } catch (e) {
          console.error('TW: Injection failed inside writeText', e);
          return originalWriteText.call(this, text);
        }
      }
      return originalWriteText.call(this, text);
    };

    // 2. Patch write
    const originalWrite = proto.write;
    proto.write = async function(items) {
      const fp = getFingerprint();
      if (!fp) return originalWrite.call(this, items);

      // Log attempt
      const code = fp.charCodeAt(0).toString(16).toUpperCase().padStart(4, '0');
      console.log(`TW [PROTO]: write interception → ${getAIName()} (U+${code})`);

      try {
        const newItems = await Promise.all(items.map(async (item) => {
          const blobs = {};
          // Reconstruct blobs with watermarked text
          for (const type of item.types) {
             const blob = await item.getType(type);
             if (type === 'text/plain') {
               const text = await blob.text();
               const watermarked = injectWatermark(text);
               blobs[type] = new Blob([watermarked], { type });
               // Notify user strictly once per batch
               showNotification(`Watermark: ${getAIName()} (U+${code})`);
             } else {
               blobs[type] = blob;
             }
          }
          return new ClipboardItem(blobs);
        }));

        return originalWrite.call(this, newItems);

      } catch (err) {
        console.error('TW: write interception error', err);
        // Fallback to original
        return originalWrite.call(this, items);
      }
    };

    console.log('TW: Clipboard prototype patching complete.');

  } else {
    console.warn('TW: Clipboard API not found in this environment.');
  }

} catch (e) {
  console.error('TW: Fatal error patching clipboard prototype', e);
}

// (Manual copy event removed - handled by content_isolated.js in ISOLATED world)

// Log activation
const activeFp = getFingerprint();
if (activeFp) {
  const c = activeFp.charCodeAt(0).toString(16).toUpperCase().padStart(4, '0');
  console.log(`TW [MAIN] Ready on ${getAIName()} (U+${c})`);
}
