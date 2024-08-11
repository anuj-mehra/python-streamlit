import camelot
from camelot.core import TableList

pdf_path = "/Users/anujmehra/git/python-streamlit/python-streamlit/camelot/SamplePDF.pdf"
##table_indices = [0, 2]  # Indices of tables you want to extract

##tables = camelot.read_pdf(pdf_path, pages='all', flavor='stream')
##selected_tables = [tables[i] for i in table_indices if i < len(tables)]

##for i, table in enumerate(selected_tables):
##    print(f"Table {i}:")
##    print(table.df)

# Reading all tables from the PDF
tables: TableList = camelot.read_pdf(pdf_path, pages='all', flavor='stream')


# Iterating over each extracted table and printing the content
for i in range(len(tables)):
    table = tables[i]  # Access each table using indexing
    print(f"Table {i + 1}:")
    print(table.df)  # Convert each table to a Pandas DataFrame and print it
    print("\n")



