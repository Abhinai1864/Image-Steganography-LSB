import streamlit as st
from pathlib import Path

from encoder import encode_image
from decoder import decode_image

st.set_page_config(page_title="Image Steganography Tool", page_icon="🔐", layout="centered")

BASE_DIR = Path(__file__).parent
INPUT_DIR = BASE_DIR / "input"
OUTPUT_DIR = BASE_DIR / "output"
INPUT_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)

st.title("🔐 Image Steganography Tool")
st.write("Hide secret messages inside images using Least Significant Bit (LSB) steganography.")
st.divider()

operation = st.radio("Choose an operation:", ["Hide Message", "Extract Message"], horizontal=True)
st.divider()

if operation == "Hide Message":
    st.subheader("📝 Hide a Secret Message")
    uploaded_image = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"], key="encode_image")
    secret_message = st.text_area("Enter your secret message:")

    if st.button("Encode Message"):
        if uploaded_image is None:
            st.error("Please upload an image.")
        elif not secret_message:
            st.error("Please enter a message.")
        else:
            try:
                input_path = INPUT_DIR / "original_image.png"
                output_path = OUTPUT_DIR / "secret_image.png"
                input_path.write_bytes(uploaded_image.getvalue())
                encode_image(str(input_path), str(output_path), secret_message)
                st.success("Message encoded successfully!")
                st.image(str(output_path), caption="Encoded Image", use_container_width=True)
                with open(output_path, "rb") as file:
                    st.download_button(
                        label="⬇️ Download Encoded Image",
                        data=file,
                        file_name="secret_image.png",
                        mime="image/png"
                    )
            except ValueError as error:
                st.error(str(error))
            except Exception as error:
                st.error(f"An error occurred: {error}")

elif operation == "Extract Message":
    st.subheader("🔍 Extract a Hidden Message")
    uploaded_image = st.file_uploader("Upload an encoded PNG image", type=["png"], key="decode_image")

    if st.button("Decode Message"):
        if uploaded_image is None:
            st.error("Please upload an encoded image.")
        else:
            try:
                input_path = INPUT_DIR / "encoded_image.png"
                input_path.write_bytes(uploaded_image.getvalue())
                decoded_message = decode_image(str(input_path))
                if decoded_message is not None:
                    st.success("Message extracted successfully!")
                    st.text_area("Extracted Secret Message:", value=decoded_message, height=150)
                else:
                    st.warning("No message could be extracted.")
            except Exception as error:
                st.error(f"An error occurred: {error}")
