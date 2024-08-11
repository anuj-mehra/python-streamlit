from typing import List, Dict, Any

import pdfplumber as pp
from pdfplumber.page import Page

pdf = pp.open("/resources/SamplePDF.pdf")

pages: list[Page] = pdf.pages

i = 0
for page in pages:
    images: list[dict[str, Any]] = page.images
    for image in images:
       print(image)
