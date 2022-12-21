import streamlit as st
from PIL import Image

with st.expander("start camera"):
    #start the camera
    camera_image = st.camera_input("camera")

if camera_image:
    #create a pillowimage instamce
    img = Image.open(camera_image)

    #convert pillow image to grayscale
    gray_image = img.convert("L")

    #render the grayscale image to webpage
    st.image(gray_image)
