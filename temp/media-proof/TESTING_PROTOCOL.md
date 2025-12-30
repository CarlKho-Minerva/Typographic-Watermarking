# Typographic Watermarking — Validation Testing Protocol

## Pre-Requisites
- [ ] Chrome extension installed and enabled
- [ ] Decoder tool (`index.html`) open in browser
- [ ] Accounts on: ChatGPT, Claude, Gemini, Copilot, Perplexity

---

## Phase 1: Extension Verification (15 min)

For **each AI platform**, verify the extension works:

### ChatGPT (chat.openai.com)
- [ ] Generate a response (any prompt, 50+ words)
- [ ] Copy via **Copy button** → Paste in decoder → Confirm U+2009 (Thin Space) detected
- [ ] Copy via **Ctrl+C** → Paste in decoder → Confirm U+2009 detected
- [ ] Screenshot result

### Claude (claude.ai)
- [ ] Generate response → Copy button → Decoder → Confirm U+200A (Hair Space)
- [ ] Ctrl+C → Decoder → Confirm U+200A
- [ ] Screenshot

### Gemini (gemini.google.com)
- [ ] Generate response → Copy button → Decoder → Confirm U+2005 (Four-Per-Em)
- [ ] Ctrl+C → Decoder → Confirm U+2005
- [ ] Screenshot

### Copilot (copilot.microsoft.com)
- [ ] Generate response → Copy → Decoder → Confirm U+2006 (Six-Per-Em)
- [ ] Screenshot

### Perplexity (perplexity.ai)
- [ ] Generate response → Copy → Decoder → Confirm U+2007 (Figure Space)
- [ ] Screenshot

---

## Phase 2: Pipeline Survival Testing (30 min)

For each target platform below, use **one watermarked text sample** (e.g., from ChatGPT) and test:

### Document Editors
| Platform | Steps | Result |
|----------|-------|--------|
| Google Docs | Paste → Select All → Copy → Decode | [ ] Pass / [ ] Fail |
| Microsoft Word | Paste → Select All → Copy → Decode | [ ] Pass / [ ] Fail |
| Apple Notes | Paste → Select All → Copy → Decode | [ ] Pass / [ ] Fail |
| Notion | Paste → Select All → Copy → Decode | [ ] Pass / [ ] Fail |

### Email Clients
| Platform | Steps | Result |
|----------|-------|--------|
| Gmail (compose) | Paste → Send to self → Open → Copy → Decode | [ ] Pass / [ ] Fail |
| Outlook (web) | Paste → Send to self → Open → Copy → Decode | [ ] Pass / [ ] Fail |

### Messaging
| Platform | Steps | Result |
|----------|-------|--------|
| Slack | Paste → Send → Copy message → Decode | [ ] Pass / [ ] Fail |
| Discord | Paste → Send → Copy message → Decode | [ ] Pass / [ ] Fail |
| iMessage (web if available) | Test if possible | [ ] Pass / [ ] Fail / [ ] N/A |

### Social Media
| Platform | Steps | Result |
|----------|-------|--------|
| Twitter/X (compose, don't send) | Paste → Copy from compose box → Decode | [ ] Pass / [ ] Fail |
| LinkedIn (compose, don't send) | Paste → Copy from compose box → Decode | [ ] Pass / [ ] Fail |

### Code Editors (Expected Failures)
| Platform | Steps | Result |
|----------|-------|--------|
| VS Code | Paste → Copy → Decode | [ ] Pass / [ ] Partial / [ ] Fail |
| Notepad (Windows) | Paste → Copy → Decode | [ ] Pass / [ ] Fail |
| TextEdit (Mac, Plain Text mode) | Paste → Copy → Decode | [ ] Pass / [ ] Fail |

### Destructive Operations
| Operation | Steps | Result |
|-----------|-------|--------|
| PDF export | Paste in Docs → Export PDF → Copy from PDF → Decode | [ ] Pass / [ ] Fail |
| Regex strip | Run `text.replace(/[\u2000-\u206F]/g, ' ')` → Decode | [ ] Fail (expected) |

---

## Phase 3: Record Results

For the paper, you need:
1. **Total samples tested**: Aim for N ≥ 10 per AI platform (50 total)
2. **Trials per pipeline**: At least 3 times each
3. **Calculate survival rate**: (watermarked spaces preserved / total spaces) × 100%

### Results Summary Template:
```
| Platform | Survival | Trials | Notes |
|----------|----------|--------|-------|
| Google Docs | X% | N | ... |
| ... | ... | ... | ... |
```

---

## Phase 4: Evidence Collection

- [ ] Save all screenshots to `/chrome-extension/evidence/`
- [ ] Record a short Loom video demonstrating end-to-end flow
- [ ] Export decoder console logs if available

---

## Time Estimate
- Phase 1: ~15 min
- Phase 2: ~30 min
- Phase 3: ~15 min (data entry)
- Phase 4: ~10 min (screenshots)

**Total: ~1 hour for full validation**
