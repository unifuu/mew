from PIL import Image
from pathlib import Path

# Open image (input.png or input.jpg)
for ext in ("png", "jpg"):
    path = Path(f"input.{ext}")
    if path.exists():
        img = Image.open(path)
        break
else:
    raise FileNotFoundError("input.png or input.jpg not found")

# Ensure image is RGBA (favicon needs this sometimes)
img = img.convert("RGBA")

# favicon.ico (multi-size)
ico_sizes = [(16, 16), (32, 32), (48, 48), (64, 64)]
img.save("favicon.ico", sizes=ico_sizes)

# favicon-16x16.png
img.resize((16, 16), Image.LANCZOS).save("favicon-16x16.png")

# favicon-32x32.png
img.resize((32, 32), Image.LANCZOS).save("favicon-32x32.png")
