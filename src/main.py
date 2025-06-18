import os
import config
from ocr_processor import process_document
from entity_extractor import (
    extract_site_id, extract_equipment, extract_quantity, extract_manufacturer,
    extract_serial_number, extract_power, extract_capacity, extract_dimensions, extract_date, extract_field
)
from csv_generator import save_to_csv

def process_all_documents():
    input_dir = config.INPUT_FOLDER
    output_dir = config.OUTPUT_FOLDER
    os.makedirs(output_dir, exist_ok=True)
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.pdf', '.png', '.jpg', '.jpeg')):
            file_path = os.path.join(input_dir, filename)
            print(f"Processing {file_path}...")
            try:
                ocr_result = process_document(file_path)
                text = ocr_result if isinstance(ocr_result, str) else str(ocr_result)
                data = {}
                # Extract all fields and confidence
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
                # Placeholder for unmapped fields
                for field in ['Category', 'Status', 'Location', 'Platform', 'Antenna Type', 'Battery Type', 'Certification', 'Inspector', 'Notes']:
                    data[field], data[f'{field} Confidence'] = extract_field(text, field)
                data['Confidence'] = min([v for k, v in data.items() if 'Confidence' in k and isinstance(v, float)], default=0.0)
                data['Source File'] = filename
                output_file = os.path.join(output_dir, filename + '.csv')
                save_to_csv(data, output_file)
                print(f"Saved results to {output_file}")
            except Exception as e:
                print(f"Error processing {file_path}: {e}")

if __name__ == "__main__":
    process_all_documents() 