"""
Typographic Watermarking: Attributing LLM Output via Unicode Substitution
A background daemon that injects invisible "fingerprints" into AI-generated text

Author: Carl Kho
License: MIT
"""

import time
import pyperclip
import subprocess

# ============================================
# UNICODE FINGERPRINTS
# These are different Unicode spaces that look identical to ASCII space
# but can be detected programmatically
# ============================================
SPACES = {
    "ChatGPT": "\u2009",  # Thin Space
    "Claude": "\u200A",   # Hair Space
    "Gemini": "\u2005",   # Four-Per-Em Space
    "Default": " "        # Standard Space (ASCII 32 / U+0020)
}

# Reverse lookup for decoder
FINGERPRINTS = {v: k for k, v in SPACES.items() if v != " "}


def get_active_window_title() -> str:
    """
    Uses AppleScript to get the name of the frontmost window.
    Works on macOS (tested on M2 Air).
    """
    script = '''
    tell application "System Events"
        set frontApp to first application process whose frontmost is true
        set windowName to name of first window of frontApp
        return windowName
    end tell
    '''
    try:
        result = subprocess.check_output(['osascript', '-e', script], stderr=subprocess.DEVNULL)
        return result.decode('utf-8').strip()
    except Exception:
        return "Unknown"


def inject_watermark(text: str, source_name: str) -> str:
    """
    Replaces standard ASCII spaces with model-specific Unicode spaces.
    """
    print(f"🕵️ Detected copy from: {source_name}")

    # Select the special space based on the source
    special_space = SPACES.get("Default")

    if "ChatGPT" in source_name or "ChatGPT" in source_name.lower():
        special_space = SPACES["ChatGPT"]
    elif "Claude" in source_name:
        special_space = SPACES["Claude"]
    elif "Gemini" in source_name:
        special_space = SPACES["Gemini"]
    else:
        print("   No AI detected, keeping standard spaces.")
        return text

    # Replace all standard spaces with the special space
    watermarked_text = text.replace(" ", special_space)
    print(f"✅ Watermark injected! Spaces replaced with {source_name} signature (U+{ord(special_space):04X}).")
    return watermarked_text


def decode_watermark(text: str) -> str:
    """
    Analyzes text and returns which AI model it came from (if any).
    """
    for char, model in FINGERPRINTS.items():
        if char in text:
            return model
    return "Unknown (No watermark detected)"


def main():
    """
    Background monitor that watches clipboard for changes.
    """
    print("=" * 50)
    print("🔒 Typographic Watermarking Daemon v0.1")
    print("=" * 50)
    print("Running background monitor...")
    print("Copy text from ChatGPT, Claude, or Gemini to inject watermark.")
    print("Press Ctrl+C to stop.\n")

    # Test clipboard access first
    try:
        test = pyperclip.paste()
        print(f"✓ Clipboard access OK (current length: {len(test)} chars)")
    except Exception as e:
        print(f"✗ Clipboard error: {e}")
        return

    # Test window detection
    window = get_active_window_title()
    print(f"✓ Window detection OK (current: '{window}')")
    print()
    print("Monitoring... (you'll see output when clipboard changes)")
    print("-" * 50)

    last_paste = pyperclip.paste()  # Initialize with current clipboard
    poll_count = 0

    while True:
        try:
            # Check current clipboard
            current_paste = pyperclip.paste()
            poll_count += 1

            # Show we're alive every 20 polls (10 seconds)
            if poll_count % 20 == 0:
                print(f"[polling... {poll_count}]", end="\r")

            # If clipboard changed (User pressed Cmd+C)
            if current_paste != last_paste:
                print(f"\n📋 Clipboard changed! Length: {len(current_paste)} chars")
                print(f"   Preview: {current_paste[:50]}..." if len(current_paste) > 50 else f"   Content: {current_paste}")

                # 1. Get the source (Window Title)
                window_title = get_active_window_title()
                print(f"   Window: '{window_title}'")

                # 2. Modify the text
                new_text = inject_watermark(current_paste, window_title)

                # 3. Update the clipboard (only if we actually changed something)
                if new_text != current_paste:
                    pyperclip.copy(new_text)
                    last_paste = new_text  # Update tracker so we don't loop forever
                    print(f"   ✓ Clipboard updated with watermark\n")
                else:
                    last_paste = current_paste
                    print()

            time.sleep(0.5)  # Check twice a second

        except KeyboardInterrupt:
            print("\n\n[+] Daemon stopped.")
            break


if __name__ == "__main__":
    main()
