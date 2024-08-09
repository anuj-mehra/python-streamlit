import camelot

def extract_tables_from_pdf(pdf_path, table_indices):
    tables = camelot.read_pdf(pdf_path, pages='all', flavor='stream')
    selected_tables = [tables[i] for i in table_indices if i < len(tables)]
    return selected_tables

def main():
    pdf_path = "/Users/anujmehra/git/python-streamlit/python-streamlit/pdfplumber/TaxData.pdf"
    table_indices = [0, 2]  # Indices of tables you want to extract

    tables = extract_tables_from_pdf(pdf_path, table_indices)

    for i, table in enumerate(tables):
        print(f"Table {i}:")
        print(table.df)

if __name__ == "__main__":
    main()


## (clustering and classification)

