from PIL import Image


def calculate_image_capacity(image_path):
    """Print theoretical RGB LSB capacity for an image."""
    with Image.open(image_path) as image:
        width, height = image.size

    total_pixels = width * height
    total_bits = total_pixels * 3
    capacity_bytes = total_bits // 8
    capacity_kb = capacity_bytes / 1024
    capacity_mb = capacity_kb / 1024

    print("\n----- IMAGE CAPACITY REPORT -----")
    print("Image dimensions:", width, "x", height)
    print("Total pixels:", total_pixels)
    print("Total available bits:", total_bits)
    print("Maximum theoretical capacity:", capacity_bytes, "bytes")
    print("Capacity in KB:", round(capacity_kb, 2), "KB")
    print("Capacity in MB:", round(capacity_mb, 2), "MB")


if __name__ == "__main__":
    image_path = input("Enter image path: ").strip()
    calculate_image_capacity(image_path)
