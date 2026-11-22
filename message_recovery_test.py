from pathlib import Path
from decoder import decode_image

test_images = [
    "output/secret_image.png",
    "images/resized.png",
    "images/cropped.png",
    "images/compressed.jpg",
]

for image_path in test_images:
    print("\n================================")
    print("Testing:", image_path)
    print("================================")
    if not Path(image_path).is_file():
        print("Image not found!")
        continue
    try:
        message = decode_image(image_path)
        if message:
            print("Recovered message:", message)
        else:
            print("No valid message recovered.")
    except Exception as error:
        print("Decoding failed:", error)
