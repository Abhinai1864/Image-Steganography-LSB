from PIL import Image
import os


def detect_lsb_changes(original_path, encoded_path):
    if not os.path.exists(original_path):
        print("Error: Original image not found!")
        return
    if not os.path.exists(encoded_path):
        print("Error: Encoded image not found!")
        return

    original = Image.open(original_path).convert("RGB")
    encoded = Image.open(encoded_path).convert("RGB")
    if original.size != encoded.size:
        print("Error: Image dimensions do not match!")
        return

    original_pixels = original.get_flattened_data()
    encoded_pixels = encoded.get_flattened_data()
    total_channels = changed_channels = lsb_changes = 0

    for original_pixel, encoded_pixel in zip(original_pixels, encoded_pixels):
        for original_value, encoded_value in zip(original_pixel, encoded_pixel):
            total_channels += 1
            if original_value != encoded_value:
                changed_channels += 1
            if (original_value & 1) != (encoded_value & 1):
                lsb_changes += 1

    change_percentage = changed_channels / total_channels * 100 if total_channels else 0
    lsb_percentage = lsb_changes / total_channels * 100 if total_channels else 0

    print("\n======================================")
    print("       LSB DETECTION ANALYSIS")
    print("======================================")
    print("Image dimensions:", original.size)
    print("Total colour channels:", total_channels)
    print("Changed colour channels:", changed_channels)
    print("Changed LSBs:", lsb_changes)
    print("--------------------------------------")
    print("Changed channel percentage:", round(change_percentage, 4), "%")
    print("Changed LSB percentage:", round(lsb_percentage, 4), "%")
    print("======================================")
    print("\nAnalysis completed successfully!")


if __name__ == "__main__":
    detect_lsb_changes("images/original.png", "output/secret_image.png")
