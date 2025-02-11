import streamlit as st
import pytesseract
from PIL import Image
import numpy as np
import easyocr

# Title
st.title("📸 Image to Text Converter")

# Upload Image
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image", use_container_width=True)

    # Convert image to array
    img_array = np.array(img)

    # Perform OCR using EasyOCR
    reader = easyocr.Reader(['en'])
    text = reader.readtext(img_array, detail=0)

    # Display Extracted Text
    st.subheader("📝 Extracted Text:")
    if text:
        st.text_area("OCR Output", " ".join(text), height=200)
    else:
        st.warning("⚠ No text detected. Try again with a clearer image.")
