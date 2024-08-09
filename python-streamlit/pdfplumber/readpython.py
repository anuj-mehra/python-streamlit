from typing import List

import pdfplumber as pp
from pdfplumber.page import Page

with pp.open("/Users/anujmehra/git/python-streamlit/python-streamlit/pdfplumber/TaxData.pdf") as pdf:
    # Extract the text
    text: list[Page] = pdf.pages
    page0: str =  text[0].extract_text()

    print(page0)



pip install "camelot-py[cv]" PyPDF2 pdfplumber


