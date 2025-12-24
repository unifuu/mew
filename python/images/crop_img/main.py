from PIL import Image

def autocrop(input_path, output_path):
    img = Image.open(input_path).convert("RGBA")

    # Get the bounding box of non-empty pixels
    bbox = img.getbbox()  # auto-detects non-black/non-transparent area

    if bbox:
        cropped = img.crop(bbox)
    else:
        cropped = img

    # Optional: Resize to make it bigger
    scale = 4  # 4x bigger
    new_size = (cropped.width * scale, cropped.height * scale)
    resized = cropped.resize(new_size, Image.NEAREST)  # NEAREST keeps pixel style

    resized.save(output_path, "PNG")

autocrop("input.png", "output.png")