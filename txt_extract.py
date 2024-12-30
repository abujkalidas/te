import cv2
import pytesseract
from PIL import Image
import streamlit as st
import numpy as np

def main():
    st.title("Webcam Video Stream with OCR")

    # Access the webcam (update URL if using an IP camera)
    url = "http://192.168.1.39:8080/video"
    video_stream = cv2.VideoCapture(0)  # Change to `0` for the default webcam

    st.subheader("Live Webcam Feed")
    video_placeholder = st.empty()
    text_placeholder = st.empty()

    # Initialize the path to Tesseract
    path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    pytesseract.pytesseract.tesseract_cmd = path_to_tesseract

    while True:
        # Read video frame
        ret, frame = video_stream.read()

        if not ret:
            st.warning("Unable to read from video stream. Please check the connection.")
            break

        # Convert BGR (OpenCV default) to RGB for Streamlit compatibility
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Display the video frame in the Streamlit app
        video_placeholder.image(frame_rgb, channels="RGB")

        # Perform OCR on a resized grayscale version of the frame
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        resized_frame = cv2.resize(gray_frame, None, fx=0.5, fy=0.5)  # Resize to speed up OCR
        text = pytesseract.image_to_string(resized_frame)

        # Display extracted text in the Streamlit app
        text_placeholder.text_area("Extracted Text", text, height=200)

        # Add an exit condition (terminate the loop with Streamlit button)
        if st.button("Stop Stream"):
            break

    # Release the video stream
    video_stream.release()

if __name__ == "__main__":
    main()
