// content.js

const SPACES = {
    "ChatGPT": "\u2009",      // Thin Space
    "Claude": "\u200A",       // Hair Space
    "Gemini": "\u2005",       // Four-Per-Em Space
    "Copilot": "\u2006",      // Six-Per-Em Space
    "Perplexity": "\u2007",   // Figure Space
    "Default": " "           // Standard Space
};

function getSiteName() {
    const host = window.location.hostname;
    if (host.includes("chatgpt.com") || host.includes("chat.openai.com")) return "ChatGPT";
    if (host.includes("claude.ai")) return "Claude";
    if (host.includes("gemini.google.com") || host.includes("googleusercontent.com")) return "Gemini";
    if (host.includes("copilot.microsoft.com")) return "Copilot";
    if (host.includes("perplexity.ai")) return "Perplexity";
    return "Default";
}

document.addEventListener("copy", (event) => {
    const selection = document.getSelection();
    const text = selection.toString();

    if (!text) return; // Nothing selected

    const siteName = getSiteName();
    const specialSpace = SPACES[siteName] || SPACES["Default"];

    console.log(`[Watermark] Intercepting copy from ${siteName}. original length: ${text.length}`);

    // Replace standard spaces AND non-breaking spaces
    const watermarkedText = text.replace(/[\u0020\u00A0]/g, specialSpace);

    console.log(`[Watermark] Injecting ${encodeURI(specialSpace)}. New text length: ${watermarkedText.length}`);

    // Overwrite the clipboard data
    event.clipboardData.setData("text/plain", watermarkedText);

    // Prevent the site's default behavior AND stop other listeners
    event.preventDefault();
    event.stopImmediatePropagation();
}, true); // TRUE = Capture Phase
