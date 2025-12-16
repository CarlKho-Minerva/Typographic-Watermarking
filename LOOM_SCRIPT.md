# Typographic Watermarking — Loom Demo Script
## Duration: 2 minutes | Last Updated: 2025-12-16 22:00 UTC+8

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

**[OPTIONAL: Quick multi-site montage - 10 seconds]**
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
> "BOOM. 100% watermarked. Source: ChatGPT."
>
> **[Hover over the visualized text, spaces highlight yellow]**
>
> "See these highlighted spots? Every single space in this text is now a special Unicode character—U+2009, the 'Thin Space'—invisibly tagged to ChatGPT.
>
> Claude gets a different space. Gemini gets another. It's like invisible ink, but for AI."

---

## 🎯 THE EXPLANATION (1:40 - 1:55)

> "I call it **Typographic Watermarking**. It's not perfect—you can strip it with regex—but for the average student copy-pasting into an essay? It works.
>
> Think of it like EXIF data for images, but for text."

---

## 📣 CALL TO ACTION (1:55 - 2:00)

> "The Chrome extension is free. The decoder is live. Link's in the description.
>
> Let me know what you think—I'm writing the arXiv paper right now."

---

## 🎥 B-ROLL SUGGESTIONS

1. **Side-by-side A vs А** — Use large font, maybe animate a swap
2. **Extension popup** — Show the fingerprint assignments
3. **Decoder results** — Confidence bar filling up
4. **Highlighted spaces** — Yellow hover effect on each space
5. **Code snippet** — The `replace(/ /g, '\u2009')` one-liner

---

## 📝 NOTES

- Keep it fast and punchy—no academic jargon
- The Cyrillic hook is the "mic drop" opener
- Show the TOAST notification when copying
- Hover over spaces in decoder for visual impact
- End with the arXiv angle to establish credibility
