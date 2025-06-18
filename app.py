import streamlit as st
import os
import tempfile
import pandas as pd
from src.ocr_processor import process_document
from src.entity_extractor import (
    extract_site_id, extract_equipment, extract_quantity, extract_manufacturer,
    extract_serial_number, extract_power, extract_capacity, extract_dimensions, extract_date, extract_field
)
from src.csv_generator import save_to_csv

st.title("Telecom Asset Extraction")
st.write("Upload German telecom inspection PDFs or images. Extracted data from all files will be combined into a single CSV download.")

uploaded_files = st.file_uploader("Upload documents", type=["pdf", "png", "jpg", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    results = []
    for uploaded_file in uploaded_files:
        with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[-1]) as tmp_file:
            tmp_file.write(uploaded_file.read())
            tmp_path = tmp_file.name
        try:
            ocr_result = process_document(tmp_path)
            text = ocr_result if isinstance(ocr_result, str) else str(ocr_result)
            data = {}
            data['TIMS Site Code'], _ = extract_site_id(text)
            data['Field Asset Name'], _ = extract_equipment(text)
            data['Quantity'], _ = extract_quantity(text)
            data['Manufacturer'], _ = extract_manufacturer(text)
            data['Serial Number'], _ = extract_serial_number(text)
            data['Power (kW)'], _ = extract_power(text)
            data['Capacity (Ah)'], _ = extract_capacity(text)
            data['Dimensions (mm)'], _ = extract_dimensions(text)
            data['Installation Date'], _ = extract_date(text)
            data['Inspection Date'], _ = extract_date(text)
            for field in ['Category', 'Status', 'Location', 'Platform', 'Antenna Type', 'Battery Type', 'Certification', 'Inspector', 'Notes']:
                data[field], _ = extract_field(text, field)
            data['Source File'] = uploaded_file.name
            results.append(data)
        except Exception as e:
            st.error(f"Error processing {uploaded_file.name}: {e}")
        finally:
            os.remove(tmp_path)
    if results:
        df = pd.DataFrame(results)
        st.success("Processing complete! Download the combined CSV below.")
        st.download_button(
            label="Download Combined CSV",
            data=df.to_csv(index=False).encode('utf-8'),
            file_name="combined_results.csv",
            mime='text/csv'
        )
        st.dataframe(df) 