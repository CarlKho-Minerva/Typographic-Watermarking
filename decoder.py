"""
Typographic Watermark Decoder
Detects which AI model generated text based on Unicode space fingerprints
"""

# Same fingerprints as daemon
FINGERPRINTS = {
    "\u2009": "ChatGPT",  # Thin Space
    "\u200A": "Claude",   # Hair Space
    "\u2005": "Gemini",   # Four-Per-Em Space
}


def decode(text: str) -> dict:
    """
    Analyze text and return detection results.
    """
    results = {
        "detected_model": None,
        "confidence": "high",
        "watermark_char": None,
        "watermark_count": 0,
    }

    for char, model in FINGERPRINTS.items():
        count = text.count(char)
        if count > 0:
            results["detected_model"] = model
            results["watermark_char"] = f"U+{ord(char):04X}"
            results["watermark_count"] = count
            break

    return results


def main():
    print("=" * 50)
    print("🔍 Typographic Watermark Decoder")
    print("=" * 50)
    print()

    text = input("Paste text here: ")

    results = decode(text)

    if results["detected_model"]:
        print()
        print(f"🚨 DETECTED: This text came from {results['detected_model']}")
        print(f"   Watermark character: {results['watermark_char']}")
        print(f"   Watermarks found: {results['watermark_count']}")
    else:
        print()
        print("❓ No watermark detected (standard ASCII spaces)")


if __name__ == "__main__":
    main()
