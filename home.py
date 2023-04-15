#tesseract
import pytesseract
from PIL import Image


#streamlit
import streamlit as st
import pandas as pd
import numpy as np
from io import StringIO

st.title('OCR Image Processor')
st.write (":green[Upload your image below.]")
uploaded_file = st.file_uploader("Choose a file", type = ["jpg", "jpeg", "png"], accept_multiple_files = True)

option = st.selectbox(
    'What language is your file in?',
    ('English', 'Chinese', 'Japanese'))

if option == 'English':
    lang = 'eng'

if option == 'Chinese':
    lang = 'chi'

if option == 'Japanese':
    lang = 'jpn'

st.write('You selected:', option)

if st.button('Process'):
   image = Image.open(
    uploaded_file)
   extracted_text = pytesseract.image_to_string(image, lang=lang) 
   st.write('Here is the text')
else:
    st.write('')

df = pd.DataFrame({
  'file': uploaded_file,
  #'Extracted text': extracted_text
})

#st.dataframe (data=extracted_text, width=None, height=None, *, use_container_width=False)
