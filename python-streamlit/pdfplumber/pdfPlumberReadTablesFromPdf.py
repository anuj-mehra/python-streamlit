from typing import List, Any

import pdfplumber
import numpy as np
from numpy import ndarray, dtype
from pyspark.sql.types import StructType, StructField, StringType

# Path to the PDF file
pdfPath = "/Users/anujmehra/git/python-streamlit/python-streamlit/resources/SamplePDF.pdf"

# Open the PDF file
with pdfplumber.open(pdfPath) as pdf:
    for page_number, page in enumerate(pdf.pages, start=1):
        print(f"Page {page_number}:")
        tables: list[list[list[str]]] = page.extract_tables()
        numberOfTables = len(tables)
        print(f"Number of Tables {numberOfTables}:")

        tableColumnslist: list[list[str]] = []
        schemas: list[StructType] = []
        for table_number, table in enumerate(tables, start=1):
            print(f"Table {table_number}:")
            if table:  # Check if the table is not empty
                first_row: list[str] = table[0]  # Get the first row
                num_columns = len(first_row)  # Get the number of columns in the first row
                print(f"Row 1 has {num_columns} columns: {first_row}")
                tableColumnslist.append(first_row)  # Add the first row to the list
            print("\n")

        for e in tableColumnslist:
            np_columns: ndarray[Any, dtype[Any]] = np.array(e)
            schema = StructType([StructField(column, StringType(), True) for column in np_columns])
            schemas.append(schema)
            print(schema)
            print("\n")

        for table_number, table in enumerate(tables, start=1):
            print(f"Table {table_number}:")
            for row_number, row in enumerate(table, start=1):
                num_columns = len(row)  # Get the number of columns in the row
                print(f"Row {row_number} has {num_columns} columns: {row}")
            print("\n")