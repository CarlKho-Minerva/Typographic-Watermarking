
from PIL import Image
import os

gif_path = "mario.gif"
try:
    with Image.open(gif_path) as im:
        print(f"Frame count: {im.n_frames}")
        print(f"Duration per frame: {im.info.get('duration', 0)} ms")
        total_duration = im.n_frames * im.info.get('duration', 100)
        print(f"Total duration: {total_duration} ms")

        # Save first frame as static
        im.seek(0)
        im.save("mario_static.png")
        print("Saved mario_static.png")
except Exception as e:
    print(f"Error: {e}")
