# Typographic Watermark

**Invisible AI Text Attribution via Unicode Substitution**

> "We shouldn't detect AI by analyzing words. We should detect it by analyzing spaces."

A Chrome extension that embeds invisible provenance metadata into AI-generated text by replacing ASCII spaces with model-specific Unicode variants.

## Features

- **Invisible fingerprints** — Looks identical, detectable programmatically
- **Multi-source detection** — Identify text even from mixed AI sources
- **Confidence metrics** — See exact watermarked vs regular space ratio
- **Zero model access needed** — Works at the copy layer, not the model layer

## Supported AIs

| AI Model | Unicode Space | Codepoint |
|----------|---------------|-----------|
| ChatGPT | Thin Space | U+2009 |
| Claude | Hair Space | U+200A |
| Gemini | Four-Per-Em | U+2005 |
| Copilot | Six-Per-Em | U+2006 |
| Perplexity | Figure Space | U+2007 |

## Installation

### Chrome Extension (Recommended)
1. Clone this repo
2. Go to `chrome://extensions/`
3. Enable **Developer mode**
4. Click **Load unpacked** → select `chrome-extension/`

### Web Detector
Visit [typographic-watermark.vercel.app](https://typographic-watermarking.vercel.app/) to paste and analyze text.

## How Detection Works

```javascript
// Each AI gets a unique "invisible" space:
const FINGERPRINTS = {
  'chatgpt.com': '\u2009',  // Thin Space
  'claude.ai': '\u200A',    // Hair Space
  'gemini.google.com': '\u2005', // Four-Per-Em
};

// When you copy, all regular spaces become fingerprinted:
text.replace(/ /g, fingerprint);
```

## Confidence Calculation

```
Watermark Confidence = (Watermarked Spaces / Total Spaces) × 100%
```

**Interpretation:**
- **100% watermarked** → Copied directly from AI with extension
- **0% watermarked** → Original text or watermark stripped
- **Mixed %** → Edited text (some parts AI, some human)
- **Multiple sources** → Text combined from different AIs

## Robustness Testing

| Platform | Survives? | Notes |
|----------|-----------|-------|
| Google Docs | ✅ 100% | Full preservation |
| Microsoft Word | ✅ 100% | Full preservation |
| Gmail / Outlook | ✅ 100% | Full preservation |
| Twitter/X | ✅ 100% | Full preservation |
| Notepad (Windows) | ❌ 0% | Converts to ASCII |
| VS Code | ⚠️ ~50% | Depends on settings |
| Plain text editors | ❌ | Usually normalize |

## Future Ideas

### Multi-Source Analysis
When text has multiple watermarks, we show all detected sources with their space counts. This reveals:
- Copy-paste from multiple AI chats
- Human editing with AI assistance
- AI-to-AI chains

### Crowdsourced Detection Database
Optionally submit anonymous detection results to build a dataset:
- What % of web content is AI-generated?
- Which AIs are most commonly mixed?
- Platform-specific survival rates

(Privacy-first: only space ratios, never actual text)

### Extended Metadata
Future versions could encode:
- Timestamp patterns (alternating space types)
- Session IDs (space sequences as binary)
- Model version (different space for GPT-4 vs GPT-4o)

## Limitations

This is **fragile by design**. It's a passive attribution layer, not DRM:
- Trivially strippable with regex
- Only works if OUR extension injected the watermark
- Not proof of AI authorship, just copy history

## Loom Script (2 min)

```
[0:00-0:10] HOOK
"Everyone's trying to detect AI by analyzing words.
I'm detecting it by analyzing... spaces."
*dramatic pause*

[0:10-0:30] THE REVEAL
*Screen share showing Chrome extension*
"I built a Chrome extension that makes AI text identifiable.
Watch this."
*Go to ChatGPT, generate text, hit copy*
*Toast notification appears*

[0:30-0:50] THE DECODER
"Now I paste into my detector..."
*Paste into web tool*
*Bar fills up: 100% watermarked, ChatGPT detected*
"Boom. It knows."

[0:50-1:10] THE TRICK
"Here's the trick: Unicode has MANY invisible spaces.
This one's U+2009, used by ChatGPT.
Claude uses U+200A. Gemini uses U+2005.
They look identical. But computers can tell."

[1:10-1:30] MULTI-SOURCE DEMO
*Grab text from Claude, paste after ChatGPT text*
*Analyze: Shows BOTH sources with space counts*
"Mixed sources? We detect both."

[1:30-1:50] THE IMPLICATIONS
"This isn't about detecting all AI text.
It's about adding an invisible barcode—metadata via typography.
If this was built into ChatGPT itself..."

[1:50-2:00] CTA
"Extension's free, link in bio.
Try fooling the detector. I dare you."
```

## arXiv Paper Structure

See `decoder.html` for full academic framing with:
- Abstract & Introduction
- Related Work (Kirchenbauer watermarking, DetectGPT)
- Methodology
- Robustness analysis
- Limitations
- References

## Contributing

Ideas welcome:
- More AI platform fingerprints
- Browser extension for Firefox/Safari
- Native app clipboard monitoring
- Academic validation studies

## License

MIT — Built by [Carl Kho](https://carlkho.com) at Sun Moon Lake, Taiwan

December 16 2025
