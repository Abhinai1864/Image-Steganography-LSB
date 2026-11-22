from PIL import Image


def text_to_binary(message):
    """Convert a text message to an 8-bit-per-character binary string."""
    return "".join(format(ord(character), "08b") for character in message)


def encode_image(input_path, output_path, message):
    """Embed a message in RGB channel LSBs and save the result as PNG."""
    image = Image.open(input_path).convert("RGB")
    binary_message = text_to_binary(message) + "00000000"  # null terminator
    pixels = list(image.get_flattened_data())
    capacity = len(pixels) * 3

    if len(binary_message) > capacity:
        raise ValueError("Message is too large for this image.")

    new_pixels = []
    bit_index = 0
    for pixel in pixels:
        channels = list(pixel)
        for i in range(3):
            if bit_index < len(binary_message):
                bit = int(binary_message[bit_index])
                channels[i] = (channels[i] & 254) | bit
                bit_index += 1
        new_pixels.append(tuple(channels))

    encoded_image = Image.new("RGB", image.size)
    encoded_image.putdata(new_pixels)
    encoded_image.save(output_path, format="PNG")
    return output_path


if __name__ == "__main__":
    print("Import encode_image from this module and call it with input, output and message paths.")
