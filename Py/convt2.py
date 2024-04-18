import os
import glob
import pandas as pd

def convert_xls_to_xlsx(folder_path):
    xls_files = glob.glob(os.path.join(folder_path, '*.xls'))

    for xls_file in xls_files:
        # Read xls file
        df = pd.read_excel(xls_file, None)

        # Create a new xlsx file
        xlsx_file = os.path.splitext(xls_file)[0] + '.xlsx'

        # Save all sheets to xlsx file
        with pd.ExcelWriter(xlsx_file) as writer:
            for sheet_name, data_frame in df.items():
                data_frame.to_excel(writer, sheet_name=sheet_name, index=False)

        print(f"{xls_file} converted to {xlsx_file}")

# Example usage
folder_path = 'C:/Anlise_dados/anlise/XLS'
convert_xls_to_xlsx(folder_path)
