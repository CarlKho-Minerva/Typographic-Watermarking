// content.js

const SPACES = {
    "ChatGPT": "\u2009",  // Thin Space
    "Claude": "\u200A",   // Hair Space
    "Gemini": "\u2005",   // Four-Per-Em Space
    "Default": " "        // Standard Space
};

function getSiteName() {
    const host = window.location.hostname;
    if (host.includes("chatgpt.com")) return "ChatGPT";
    if (host.includes("claude.ai")) return "Claude";
    if (host.includes("gemini.google.com")) return "Gemini";
    return "Default";
}

document.addEventListener("copy", (event) => {
    const selection = document.getSelection();
    // Use selection.toString() for plain text.
    // Note: This might lose rich formatting, but guarantees the watermark is applied to the plain text payload.
    const text = selection.toString();

    if (!text) return; // Nothing selected

    const siteName = getSiteName();
    const specialSpace = SPACES[siteName] || SPACES["Default"];

    console.log(`[Watermark] Intercepting copy from ${siteName}. original length: ${text.length}`);

    // Replace standard spaces AND non-breaking spaces (common in web rendering)
    // \u0020 is standard space, \u00A0 is non-breaking space
    const watermarkedText = text.replace(/[\u0020\u00A0]/g, specialSpace);

    console.log(`[Watermark] Injecting ${encodeURI(specialSpace)}. New text length: ${watermarkedText.length}`);

    // Overwrite the clipboard data
    event.clipboardData.setData("text/plain", watermarkedText);

    // Prevent the site's default behavior AND stop other listeners (like the site's own copy handler)
    event.preventDefault();
    event.stopImmediatePropagation();
}, true); // TRUE = Capture Phase (Runs before the website's own bubble-phase listeners)
