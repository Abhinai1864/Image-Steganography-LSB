# Image Steganography Tool using LSB

A Python and Streamlit educational project that hides text messages inside RGB images using the Least Significant Bit (LSB) technique and extracts them later.

## Features
- Upload PNG, JPG or JPEG images for message embedding.
- Hide a text message in RGB channel LSBs.
- Download the encoded image as PNG.
- Extract the hidden message from an encoded PNG.
- Run LSB-change analysis and supporting image-capacity and manipulation experiments.

## Technology stack
- Python
- Streamlit
- Pillow (PIL)
- RGB pixel manipulation
- PNG

## Project structure
- `app.py` — Streamlit interface
- `encoder.py` — converts the message to bits and embeds them in RGB LSBs
- `decoder.py` — extracts the message from RGB LSBs
- `lsb_detection_test.py` — compares original and encoded channel values and LSBs
- `security_tests.py` — calculates theoretical image capacity
- `image_manipulation_test.py` — demonstrates resize, crop and JPEG compression
- `message_recovery_test.py` — tests extraction across manipulated images
- `phase1.py` — small ASCII-to-binary demonstration
- `requirements.txt` — Python dependencies

## Setup (Windows PowerShell)
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Run the application
```powershell
python -m streamlit run app.py
```
Open the local URL printed by Streamlit (normally http://localhost:8501).

## Run the analysis scripts
Run from the repository root after creating the appropriate test images:
```powershell
python lsb_detection_test.py
python security_tests.py
python image_manipulation_test.py
python message_recovery_test.py
```
The test scripts use relative paths. The LSB detector expects `images/original.png` and `output/secret_image.png`. The manipulation and recovery scripts expect their corresponding generated files; adjust paths in the scripts when testing a different image.

## Example analysis result
A demonstrated run on a 1600 × 1024 image reported:
- Total colour channels: 4,915,200
- Changed colour channels: 88
- Changed LSBs: 88
- Changed channel percentage: 0.0018%
- Changed LSB percentage: 0.0018%

This result applies only to that particular test image and message. A low percentage of modified channels does **not** prove that the payload is undetectable.

## Security considerations and limitations
- The message is not encrypted. Steganography alone does not provide confidentiality.
- LSB patterns may be identified by statistical steganalysis.
- Resizing, cropping, colour conversion and lossy JPEG compression can damage or destroy the embedded message.
- The implementation uses a null-byte terminator; embedded text containing a null character is not supported.
- This is an educational prototype, not a production secure-communication tool.

## Credits
Cybersecurity learning project prepared for Techvedu.
