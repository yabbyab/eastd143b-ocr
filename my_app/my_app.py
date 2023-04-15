#install Open CV and Pytesseract in command line
    #pip install opencv-python
    #pip install pytesseract
#may need to install libgl1-mesa-glx separately
    #run the following:
    #sudo apt-get update
    #sudo apt-get install libgl1-mesa-glx
#to open streamlit page run:
    #streamlit run my_app.py --server.enableCORS=false

import base64
import cv2

#for tesseract ocr
import pytesseract
from PIL import Image

#for streamlit
import streamlit as st
import pandas as pd
import numpy as np

#Heading
st.title('OCR Image Processor')
st.write (":green[Upload your image below.]")

#File uploader
uploaded_file = st.file_uploader("Choose a file", type = ["jpg", "jpeg", "png"], accept_multiple_files = False)
#FIX MAX UPLOAD SIZE? via global configs?
st.write (uploaded_file)
if uploaded_file is not None:
    st.write (uploaded_file.name)

#Select box
option = st.selectbox(
    'What language is your file in?',
    ('English', 'Japanese'))
st.write('You selected:', option)

#Lang --> tesseract
if option == 'English':
    lang = 'eng'

if option == 'Japanese':
    lang = 'jpn'

if st.button('Process'):
    image = cv2.imread('/workspaces/eastd143b-ocr/my_app/'+uploaded_file.name)
    extracted_text = pytesseract.image_to_string(image, lang=lang) 
    st.write('Here is the text:')
    st.write(extracted_text)
    # Create a simple dataframe
    if uploaded_file is not None:
        df = pd.DataFrame({
            'File': [uploaded_file.name],
            'Extracted Text': [extracted_text]
        })
        # Display the dataframe in Streamlit
        st.dataframe(df)

        # Add a button to download the dataframe as a CSV file
        if st.button('Download CSV'):
            csv = df.to_csv(index=False)
            #Create a link for downloading the CSV file
            b64 = base64.b64encode(csv.encode()).decode()  # encode the CSV data as base64 string
            href = f'<a href="data:file/csv;base64,{b64}" download="mydata.csv">Download CSV file</a>'
            st.markdown(href, unsafe_allow_html=False)
else:
    st.write('')






