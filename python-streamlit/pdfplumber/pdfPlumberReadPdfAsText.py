from typing import List, Dict, Any

import pdfplumber as pp
from pdfplumber.page import Page

pdf = pp.open("/resources/SamplePDF.pdf")

pages: list[Page] = pdf.pages

i = 0
for page in pages:
    text: str = page.extract_text()
    table: list[list[str | None]] | None = page.extract_table()
    words: list[dict[str, Any]] = page.extract_words()
    print("page",i," text")
    print(text)

