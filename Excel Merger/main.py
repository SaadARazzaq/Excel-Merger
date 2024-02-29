import streamlit as st
import pandas as pd
from io import BytesIO

def merge_files(files):
    merged_data = pd.DataFrame()
    
    for file_name, file_content in files.items():
        try:
            if file_name.endswith('.xlsx') or file_name.endswith('.xls'):
                data = pd.read_excel(file_content, engine='openpyxl')
            elif file_name.endswith('.csv'):
                data = pd.read_csv(file_content)
            else:
                st.error(f"Unsupported file format: {file_name}")
                continue

            if merged_data.empty:
                merged_data = data
            else:
                duplicate_columns = set(merged_data.columns).intersection(set(data.columns))  # Drop duplicate columns
                data = data.drop(columns=duplicate_columns)
                merged_data = pd.concat([merged_data, data], axis=1)

        except Exception as e:
            st.error(f"Error reading file {file_name}: {e}")
            continue  # Skip to the next file if an error occurs

    return merged_data

def main():
    st.title("Excel Merger")

    st.write("Upload files:")
    uploaded_files = st.file_uploader("Choose files", accept_multiple_files=True)

    if uploaded_files:
        merged_data = merge_files({file.name: file for file in uploaded_files})

        st.write("Merged Data:")
        st.dataframe(merged_data)
        
        st.write(f"Total Columns: {len(merged_data.columns)}")

        excel_file = BytesIO()
        with pd.ExcelWriter(excel_file, engine='xlsxwriter') as writer:
            merged_data.to_excel(writer, index=False)
        excel_file.seek(0)
        st.markdown("### Download Merged Data")
        st.write("Click below to download the merged data as an Excel file.")
        st.download_button(label="Download Merged Data", data=excel_file, file_name="merged_data.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

if __name__ == "__main__":
    main()