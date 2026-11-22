from PIL import Image


def decode_image(input_path):
    """Extract a null-terminated message from RGB channel LSBs."""
    image = Image.open(input_path).convert("RGB")
    pixels = list(image.getdata())
    decoded_message = ""

    byte_bits = ""
    for pixel in pixels:
        for color_value in pixel:
            byte_bits += str(color_value & 1)
            if len(byte_bits) == 8:
                ascii_value = int(byte_bits, 2)
                if ascii_value == 0:
                    return decoded_message
                decoded_message += chr(ascii_value)
                byte_bits = ""

    return decoded_message


if __name__ == "__main__":
    image_path = "output/secret_image.png"
    message = decode_image(image_path)
    print("\nExtracted Secret Message:")
    print(message)
