from PIL import Image, ImageSequence
import os

def trim_gif(input_path, output_gif, output_static):
    im = Image.open(input_path)

    # 1. Calculate the bounding box of ALL frames combined
    # We need to look at the alpha channel or background color

    frames = [frame.copy() for frame in ImageSequence.Iterator(im)]

    # Initialize min/max coordinates
    min_x, min_y = im.width, im.height
    max_x, max_y = 0, 0

    found_content = False

    for frame in frames:
        # Convert to RGBA to checking alpha
        rgba = frame.convert("RGBA")
        bbox = rgba.getbbox() # Returns (left, upper, right, lower)

        if bbox:
            found_content = True
            min_x = min(min_x, bbox[0])
            min_y = min(min_y, bbox[1])
            max_x = max(max_x, bbox[2])
            max_y = max(max_y, bbox[3])

    if not found_content:
        print("No content found in gif!")
        return

    # Add a small padding if desired, or just crop tight
    # User said "trim the gif and img", implying tight crop.

    crop_box = (min_x, min_y, max_x, max_y)
    print(f"Original size: {im.width}x{im.height}")
    print(f"Cropping to: {crop_box}")
    print(f"New size: {max_x - min_x}x{max_y - min_y}")

    # 2. Crop all frames
    cropped_frames = []
    for frame in frames:
        # We must preserve the disposal/duration info
        # frame.crop returns a copy
        cropped = frame.crop(crop_box)
        cropped_frames.append(cropped)

    # 3. Save trimmed GIF
    # Use info from original image for duration/loop
    duration = im.info.get('duration', 100)
    loop = im.info.get('loop', 0)

    cropped_frames[0].save(
        output_gif,
        save_all=True,
        append_images=cropped_frames[1:],
        duration=duration,
        loop=loop,
        disposal=2 # Restore to background color
    )
    print(f"Saved trimmed GIF to {output_gif}")

    # 4. Save static image (first frame of trimmed gif)
    cropped_frames[0].save(output_static)
    print(f"Saved trimmed static to {output_static}")

if __name__ == "__main__":
    trim_gif('mario.gif', 'mario_trimmed.gif', 'mario_static_trimmed.png')
