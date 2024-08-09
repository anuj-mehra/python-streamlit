url = "/Users/anujmehra/git/python-streamlit/python-streamlit/pdfplumber/TaxData.pdf"

import pdfplumber

pdf = pdfplumber.open(url)

for page in range(0:len(pdf.pages)):
    if 'Total number of physical restraints' in pdf.pages[page]:
        print(pdf.page_number)