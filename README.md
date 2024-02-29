# Excel Merger 📊

## Overview ℹ️
The "Excel Merger" is a Streamlit app designed to merge multiple Excel (.xlsx, .xls) and CSV files into a single merged file. It allows users to upload multiple files, merges them while dropping duplicate columns, displays the merged data along with the total column count, and provides an option to download the merged data as an Excel file.

## Flow of the Program 🔄
1. **Upload Files**: Users are prompted to upload Excel or CSV files by clicking on the "Choose files" button.
2. **Merge Files**: The uploaded files are processed one by one. For each file, the app checks the file format and reads it accordingly using Pandas. Excel files are read with the 'openpyxl' engine, while CSV files are read using the default engine. Duplicate columns are dropped to ensure that each column is unique in the merged dataset.
3. **Display Merged Data**: The merged data is displayed in a DataFrame format using Streamlit's `st.dataframe()` function. Additionally, the total column count of the merged DataFrame is shown.
4. **Download Merged Data**: Users can download the merged data as an Excel file by clicking on the "Download Merged Data" button. The merged data is written to an Excel file in memory and provided as a downloadable link.

## Usage 🚀
- **Data Integration**: The app is useful for integrating data from multiple Excel or CSV files into a single dataset, which can be further analyzed or used for reporting purposes.
- **Data Cleanup**: It can also be used for cleaning up redundant data across multiple files by merging them and removing duplicate columns.
- **Data Export**: Users can export merged data as an Excel file for offline analysis or sharing with others.

## Supported File Formats 📄
- **Input**: Excel (.xlsx, .xls) and CSV
- **Output**: Excel (.xlsx)

## Running the App 🏃‍♂️
To run the app locally:
1. Install the required dependencies using `pip install -r requirements.txt`.
2. Execute the script `main.py`.
3. Access the app through the provided local URL in the terminal.

## Example 📝
Suppose you have several Excel files containing sales data for different regions. You can use this app to merge these files into a single dataset, making it easier to analyze overall sales performance across regions.

## Note 📌
- Ensure that the uploaded files are in the supported formats (.xlsx, .xls, .csv) and contain structured data for successful merging.
- The app may encounter errors if the uploaded files are corrupted or in an unsupported format. Error messages will be displayed accordingly.
