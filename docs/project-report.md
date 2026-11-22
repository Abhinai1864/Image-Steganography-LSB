# Project Report: Image Steganography Tool using LSB

**Project platform:** Techvedu  
**Course:** Cybersecurity  
**Project author:** Maddela Abhinai

## Abstract
This project demonstrates image steganography by embedding a text message into the least significant bits (LSBs) of the red, green and blue channels of an image. A Streamlit interface provides a hide-message flow and an extract-message flow. Additional scripts examine image capacity, compare original and encoded channel values, and test image transformations.

## 1. Introduction
Steganography conceals the existence of information inside an ordinary carrier. This project uses an RGB image as the carrier and stores message bits in channel LSBs. The encoded image is saved as PNG so the pixel values are retained without lossy JPEG recompression.

## 2. Problem Statement
Build a simple tool that embeds text into an image, extracts it again, and demonstrates relevant security implications and limitations of basic LSB steganography.

## 3. Objectives
- Implement RGB LSB message embedding and extraction.
- Provide a user-friendly Streamlit interface.
- Check message recovery from an encoded PNG.
- Measure pixel-channel and LSB changes.
- Discuss detectability, capacity and robustness limits.

## 4. Technologies
Python, Streamlit, Pillow (PIL), RGB image processing and PNG.

## 5. Methodology
**Encoding:** Convert each message character to an 8-bit binary representation, append an 8-bit zero terminator, then replace successive RGB channel LSBs with message bits. Save the modified image as PNG.

**Decoding:** Traverse the encoded image's RGB channels in the same order, collect each channel's LSB, group the bits into bytes, convert bytes to characters and stop at the null-byte terminator.

**Theoretical capacity:** RGB LSB storage offers up to width × height × 3 bits. The practical message capacity is slightly lower because the terminator also occupies bits.

## 6. Application Modules
- `app.py`: Streamlit interface for upload, hide, extract and download.
- `encoder.py`: message conversion and LSB embedding.
- `decoder.py`: LSB extraction and message reconstruction.
- `lsb_detection_test.py`: original-versus-encoded colour channel comparison.
- `security_tests.py`: theoretical image capacity calculation.
- `image_manipulation_test.py`: resize, crop and JPEG compression experiments.
- `message_recovery_test.py`: recovery checks on original and manipulated output files.

## 7. Demonstrated Functional Test
The message **“Hello Good Morning”** was successfully encoded using the Streamlit interface and subsequently extracted from the encoded image.

## 8. LSB Detection Analysis
The reported Phase 5 test output was:

| Metric | Result |
|---|---:|
| Image dimensions | 1600 × 1024 |
| Total colour channels | 4,915,200 |
| Changed colour channels | 88 |
| Changed LSBs | 88 |
| Changed channel percentage | 0.0018% |
| Changed LSB percentage | 0.0018% |

The percentages are rounded to four decimal places. The result describes this particular sample image and message only. A low modification rate does not prove that the hidden data is undetectable.

## 9. Security Implications and Limitations
- The message is not encrypted; LSB steganography alone does not provide confidentiality.
- Statistical steganalysis may detect altered LSB distributions.
- Resizing, cropping, colour conversion and lossy JPEG compression can corrupt the hidden message.
- The null-byte terminator means a null character cannot be represented within a message.
- This implementation is an educational prototype, not a production secure communication tool.

## 10. Future Enhancements
Encrypt the payload before embedding, add explicit payload length and integrity checking, test more steganalysis methods, and investigate error-correcting codes or transform-domain techniques.

## 11. Conclusion
The project demonstrates a complete basic workflow for hiding text in RGB image LSBs and recovering it through a Streamlit interface. The test message was recovered successfully. The experiments also show why low pixel modification alone should not be confused with strong security or robustness.

## References
- Python documentation: https://docs.python.org/
- Streamlit documentation: https://docs.streamlit.io/
- Pillow documentation: https://pillow.readthedocs.io/
