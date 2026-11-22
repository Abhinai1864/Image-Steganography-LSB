from PIL import Image
from pathlib import Path

image_path = input("Enter encoded image path: ").strip()
if not Path(image_path).is_file():
    raise FileNotFoundError(f"Image not found: {image_path}")

image = Image.open(image_path).convert("RGB")
image_dir = Path("images")
image_dir.mkdir(exist_ok=True)

resized = image.resize((800, 512))
resized.save(image_dir / "resized.png")
print("1. Resized image created successfully!")

width, height = image.size
cropped = image.crop((0, 0, width // 2, height // 2))
cropped.save(image_dir / "cropped.png")
print("2. Cropped image created successfully!")

image.save(image_dir / "compressed.jpg", quality=50)
print("3. Compressed JPEG created successfully!")
print("\nImage manipulation tests completed!")
