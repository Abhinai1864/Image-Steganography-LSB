# Image Steganography Tool (LSB)

A Python + Streamlit educational project that hides text messages inside RGB images using Least Significant Bit (LSB) steganography and extracts them later.

## Features
- Hide a text message in an image.
- Export the encoded image as PNG.
- Extract a hidden message from an encoded PNG.
- Run LSB modification analysis and supporting security experiments.

## Tech Stack
Python, Streamlit, Pillow (PIL), RGB pixel manipulation, PNG.

## Setup
```bash
python -m venv .venv
# Windows PowerShell
.venv\\Scripts\\Activate.ps1
python -m pip install -r requirements.txt
```

## Run
```bash
python -m streamlit run app.py
```
Open the local URL printed by Streamlit (usually http://localhost:8501).

## Security Notes
This is an educational prototype, not a secure messaging system. The hidden text is not encrypted. Basic LSB embedding may be detectable by statistical steganalysis. Resizing, cropping, format conversion and lossy JPEG compression can damage embedded data. A small pixel-change percentage does not prove undetectability.
