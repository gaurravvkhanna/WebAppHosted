import streamlit as st
from PIL import Image

camera_image = st.camera_input("Take a picture")

img = Image.open(camera_image)

img = img.convert("L")

st.write(img)