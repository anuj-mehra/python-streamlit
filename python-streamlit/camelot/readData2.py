import camelot
import pdfplumber


def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        all_text = ""
        for page in pdf.pages:
            text = page.extract_text()
            all_text += text + "\n"
        return all_text


def extract_tables_from_pdf(pdf_path):
    try:
        tables = camelot.read_pdf(pdf_path, pages='all', flavor='stream')
        return tables
    except Exception as e:
        print(f"Error extracting tables: {e}")
        return None


def main():
    pdf_path = "/Users/anujmehra/git/python-streamlit/python-streamlit/pdfplumber/TaxData.pdf"

    # Extract and print text
    print("Extracting text from the PDF:")
    text = extract_text_from_pdf(pdf_path)
    print(text)

    # Extract and print tables
    print("\nExtracting tables from the PDF:")
    tables = extract_tables_from_pdf(pdf_path)

    if tables:
        for i, table in enumerate(tables):
            print(f"\nTable {i + 1}:")
            print(table.df)  # Print as DataFrame
    else:
        print("No tables found or an error occurred.")


if __name__ == "__main__":
    main()
