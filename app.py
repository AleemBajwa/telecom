import streamlit as st
import os
import tempfile
from src.ocr_processor import process_document
from src.entity_extractor import (
    extract_site_id, extract_equipment, extract_quantity, extract_manufacturer,
    extract_serial_number, extract_power, extract_capacity, extract_dimensions, extract_date, extract_field
)
from src.csv_generator import save_to_csv

st.title("Telecom Asset Extraction")
st.write("Upload German telecom inspection PDFs or images. Extracted data will be available as a CSV download.")

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
            data['TIMS Site Code'], data['TIMS Site Code Confidence'] = extract_site_id(text)
            data['Field Asset Name'], data['Field Asset Name Confidence'] = extract_equipment(text)
            data['Quantity'], data['Quantity Confidence'] = extract_quantity(text)
            data['Manufacturer'], data['Manufacturer Confidence'] = extract_manufacturer(text)
            data['Serial Number'], data['Serial Number Confidence'] = extract_serial_number(text)
            data['Power (kW)'], data['Power (kW) Confidence'] = extract_power(text)
            data['Capacity (Ah)'], data['Capacity (Ah) Confidence'] = extract_capacity(text)
            data['Dimensions (mm)'], data['Dimensions (mm) Confidence'] = extract_dimensions(text)
            data['Installation Date'], data['Installation Date Confidence'] = extract_date(text)
            data['Inspection Date'], data['Inspection Date Confidence'] = extract_date(text)
            for field in ['Category', 'Status', 'Location', 'Platform', 'Antenna Type', 'Battery Type', 'Certification', 'Inspector', 'Notes']:
                data[field], data[f'{field} Confidence'] = extract_field(text, field)
            data['Confidence'] = min([v for k, v in data.items() if 'Confidence' in k and isinstance(v, float)], default=0.0)
            data['Source File'] = uploaded_file.name
            # Save to CSV in temp dir
            csv_path = os.path.join(tempfile.gettempdir(), uploaded_file.name + '.csv')
            save_to_csv(data, csv_path)
            with open(csv_path, 'rb') as f:
                st.download_button(
                    label=f"Download CSV for {uploaded_file.name}",
                    data=f,
                    file_name=uploaded_file.name + '.csv',
                    mime='text/csv'
                )
            results.append(data)
        except Exception as e:
            st.error(f"Error processing {uploaded_file.name}: {e}")
        finally:
            os.remove(tmp_path)
    if results:
        st.success("Processing complete! Download your CSV files above.") 