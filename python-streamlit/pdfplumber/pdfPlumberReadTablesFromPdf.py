import pdfplumber

# Path to the PDF file
pdfPath = "/Users/anujmehra/git/python-streamlit/python-streamlit/resources/SamplePDF.pdf"

# Open the PDF file
with pdfplumber.open(pdfPath) as pdf:
    for page_number, page in enumerate(pdf.pages, start=1):
        print(f"Page {page_number}:")
        tables = page.extract_tables()

        for table_number, table in enumerate(tables, start=1):
            print(f"Table {table_number}:")
            for row_number, row in enumerate(table, start=1):
                num_columns = len(row)  # Get the number of columns in the row
                print(f"Row {row_number} has {num_columns} columns: {row}")
            print("\n")