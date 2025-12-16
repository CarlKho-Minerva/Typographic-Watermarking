import time
import pyperclip
from AppKit import NSWorkspace
import subprocess

# 1. Define your "Fingerprints"
# These are different Unicode spaces that look empty but have different IDs
SPACES = {
    "ChatGPT": "\u2009",  # Thin Space
    "Claude": "\u200A",   # Hair Space
    "Gemini": "\u2005",   # Four-Per-Em Space
    "Default": " "        # Standard Space (ASCII 32)
}

def get_active_window_title():
    # Uses AppleScript to get the name of the frontmost window
    # This works on your M2 Air
    script = 'tell application "System Events" to get name of first window of (first application process whose frontmost is true)'
    try:
        result = subprocess.check_output(['osascript', '-e', script])
        return result.decode('utf-8').strip()
    except:
        return "Unknown"

def inject_watermark(text, source_name):
    print(f"🕵️ Detected copy from: {source_name}")

    # Select the special space based on the source
    special_space = SPACES.get("Default")
    if "ChatGPT" in source_name:
        special_space = SPACES["ChatGPT"]
    elif "Claude" in source_name:
        special_space = SPACES["Claude"]
    elif "Gemini" in source_name:
        special_space = SPACES["Gemini"]
    else:
        print("No AI detected, keeping standard spaces.")
        return text

    # Replace all standard spaces with the special space
    watermarked_text = text.replace(" ", special_space)
    print(f"✅ Watermark injected! Spaces replaced with {source_name} signature.")
    return watermarked_text

def main():
    print("running background monitor...")
    last_paste = ""

    while True:
        # Check current clipboard
        current_paste = pyperclip.paste()

        # If clipboard changed (User pressed Cmd+C)
        if current_paste != last_paste:

            # 1. Get the source (Window Title)
            window_title = get_active_window_title()

            # 2. Modify the text
            new_text = inject_watermark(current_paste, window_title)

            # 3. Update the clipboard (only if we actually changed something)
            if new_text != current_paste:
                pyperclip.copy(new_text)
                last_paste = new_text # Update tracker so we don't loop forever
            else:
                last_paste = current_paste

        time.sleep(0.5) # Check twice a second

if __name__ == "__main__":
    main()
