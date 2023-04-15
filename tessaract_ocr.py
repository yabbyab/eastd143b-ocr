#tesseract
import streamlit as st
import pandas as pd
import pytesseract
from PIL import Image

#streamlit
import streamlit as st
import pandas as pd
from io import StringIO

lang = 'eng'
image = cv2.imread(
        uploaded_file)
    
extracted_text = pytesseract.image_to_string(image, lang=lang)

df = pd.DataFrame({
  'file': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:

    def analyze_image {

    

}