# Typographic Watermarking — Loom Demo Script
## Duration: 2 minutes | Last Updated: 2025-12-28 23:00 UTC+8

---

## 🎬 THE HOOK (0:00 - 0:25)

**[Face camera, holding keyboard]**

> "Look at your keyboard. Press 'A'. Now—here's a Cyrillic 'A'."
>
> **[Show side-by-side: А vs A]**
>
> "They look identical, right? But to a computer, they're completely different characters. This is how hackers create fake websites—goооgle.com with Cyrillic 'o's.
>
> I realized we can use this same trick... for good."

---

## 🔍 THE PROBLEM (0:25 - 0:45)

**[Screen share: Show OpenAI's discontinued AI classifier announcement]**

> "Everyone's trying to detect AI text by analyzing the *words*. Even OpenAI gave up—they discontinued their classifier in 2023. It just doesn't work.
>
> So I asked: what if we don't look at the text? What if we look at the *spaces*?"

---

## ⚙️ THE DEMO (0:45 - 1:15)

**[Screen share: Show ChatGPT with extension installed]**

> "Here's ChatGPT. I've installed my Chrome extension called 'Typographic Watermark.'"
>
> **[Generate a short response in ChatGPT]**
>
> "Now watch—I'll copy this using the copy button."
>
> **[Click copy button, show toast notification: "✓ ChatGPT watermark injected"]**
>
> "Looks normal, right? I'll paste it into Google Docs..."
>
> **[Paste into Google Docs—looks completely normal]**
>
> "Totally innocent."

**[Quick multi-site montage - 10 seconds]**
> "And it works everywhere—Claude, Gemini, Perplexity..."
>
> **[Quick cut: copy from Claude → toast shows "Claude", copy from Gemini → toast shows "Gemini"]**

---

## 🚨 THE REVEAL (1:15 - 1:40)

**[Switch to decoder tool]**

> "But now—watch this. I paste it into my decoder..."
>
> **[Paste text, click Analyze]**
>
> "BOOM. 88% watermarked. Source detected: ChatGPT and Gemini—I mixed text from both!"
>
> **[Hover over the visualized text, spaces highlight in their source colors - green for ChatGPT, blue for Gemini]**
>
> "See these highlighted spots? Each color is a different AI. Green spaces are ChatGPT. Blue spaces are Gemini. It's like invisible ink—carrying its source identity in every space character."

---

## 🎯 THE FRAMING (1:40 - 1:55)

> "Now—I'm not building a surveillance tool. I'm not here to 'catch' anyone.
>
> The real threat is a future where we can't tell what's real—fabricated political statements, AI-generated evidence, synthetic media with no paper trail.
>
> **Typographic Watermarking** is a proposal: what if every AI company—OpenAI, Anthropic, Google—added this to their response layer? One line of code. Invisible to users. But traceable when needed.
>
> Think of it like EXIF data for AI text. It won't stop bad actors—they can strip it—but it gives us a baseline for authenticity."

---

## 📣 CALL TO ACTION (1:55 - 2:00)

> "The Chrome extension is free. The decoder is live. Link's in the description.
>
> If you think transparent AI matters, share this. The arXiv paper is live."

---

## 🎥 B-ROLL CHECKLIST (All Captured)

- [x] Side-by-side A vs А — Cyrillic comparison
- [x] Extension popup — Fingerprint assignments
- [x] ChatGPT copy → toast notification
- [x] Claude copy → toast notification
- [x] Gemini copy → toast notification
- [x] Decoder results — Multi-source detection (ChatGPT + Gemini)
- [x] Highlighted spaces — Color-coded by source
- [x] Google Docs paste — Watermark survives
- [x] Code snippet — The `replace(/ /g, '\u2009')` one-liner

---

## 📝 NOTES

- Keep it fast and punchy—no academic jargon
- The Cyrillic hook is the "mic drop" opener
- Show the TOAST notification when copying
- Hover over spaces in decoder for visual impact
- **Reframed**: Not "catching students" → "proposal for AI companies to adopt"
- End with the arXiv angle to establish credibility
