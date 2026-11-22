# Presentation Outline: Image Steganography Tool using LSB

**Techvedu Cybersecurity Project — Maddela Abhinai**

1. **Title** — Image Steganography Tool using Least Significant Bit (LSB) Technique.
2. **Project Overview** — Hide text in RGB images and extract it later through a Streamlit application.
3. **Objectives** — Implement embedding and extraction, validate recovery, examine channel changes and explain security implications.
4. **Technology Stack** — Python, Streamlit, Pillow, RGB pixels and PNG.
5. **LSB Encoding** — Convert characters to bits, append a null-byte terminator, and replace successive RGB channel LSBs.
6. **Decoding Workflow** — Read channel LSBs, group into bytes, reconstruct characters and stop at the terminator.
7. **Application Modules** — app.py, encoder.py, decoder.py and the security/robustness test scripts.
8. **Functional Demonstration** — “Hello Good Morning” encoded successfully and then recovered by the decoder.
9. **LSB Analysis Results** — 4,915,200 total colour channels; 88 changed colour channels; 88 changed LSBs; 0.0018% changed-channel and LSB percentages.
10. **Security Implications** — The message is not encrypted; statistical detection may be possible; lossy image operations can damage the payload.
11. **Limitations and Future Work** — Add encryption, framing, integrity checks, error correction and steganalysis experiments.
12. **Conclusion** — The prototype demonstrates a working LSB hide/extract workflow and highlights its security limitations.
13. **Thank You** — Questions and discussion.
