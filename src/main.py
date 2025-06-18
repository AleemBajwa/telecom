import os
from datetime import datetime
from src import config
from src.ocr_processor import process_document
from src.entity_extractor import (
    extract_site_id, extract_equipment, extract_quantity, extract_manufacturer,
    extract_serial_number, extract_power, extract_capacity, extract_dimensions, extract_date, extract_field, extract_detected_terms
)
from src.csv_generator import save_to_csv
import pandas as pd

def extract_context_for_terms(text, terms):
    # Extract a line or two of context around each detected term
    context = {}
    lines = text.splitlines()
    for term in terms:
        for i, line in enumerate(lines):
            if term.lower() in line.lower():
                # Get the line and one before/after for context
                context[term] = '\n'.join(lines[max(0, i-1):min(len(lines), i+2)])
    return context

def process_all_documents():
    input_dir = config.INPUT_FOLDER
    output_dir = config.OUTPUT_FOLDER
    os.makedirs(output_dir, exist_ok=True)
    log_lines = []
    all_data = []
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.pdf', '.png', '.jpg', '.jpeg')):
            file_path = os.path.join(input_dir, filename)
            print(f"Processing {file_path}...")
            try:
                ocr_result = process_document(file_path)
                text = ocr_result if isinstance(ocr_result, str) else str(ocr_result)
                data = {}
                field_conf = {}
                data['TIMS Site Code'], field_conf['TIMS Site Code'] = extract_site_id(text)
                data['Field Asset Name'], field_conf['Field Asset Name'] = extract_equipment(text)
                data['Quantity'], field_conf['Quantity'] = extract_quantity(text)
                data['Manufacturer'], field_conf['Manufacturer'] = extract_manufacturer(text)
                data['Serial Number'], field_conf['Serial Number'] = extract_serial_number(text)
                data['Power (kW)'], field_conf['Power (kW)'] = extract_power(text)
                data['Capacity (Ah)'], field_conf['Capacity (Ah)'] = extract_capacity(text)
                data['Dimensions (mm)'], field_conf['Dimensions (mm)'] = extract_dimensions(text)
                data['Installation Date'], field_conf['Installation Date'] = extract_date(text)
                data['Inspection Date'], field_conf['Inspection Date'] = extract_date(text)
                for field in ['Category', 'Status', 'Location', 'Platform', 'Antenna Type', 'Battery Type', 'Certification', 'Inspector', 'Notes']:
                    data[field], field_conf[field] = extract_field(text, field)
                data['Confidence'] = min([v for v in field_conf.values() if isinstance(v, float)], default=0.0)
                data['Source File'] = filename
                # Extract glossary terms and context
                glossary_terms, _ = extract_detected_terms(text)
                data['Glossary Terms'] = glossary_terms
                if glossary_terms:
                    context = extract_context_for_terms(text, glossary_terms.split('; '))
                    # Optionally, add context to Notes or a new field
                    if context:
                        data['Notes'] += '\n' + '\n'.join([f"{k}: {v}" for k, v in context.items()])
                all_data.append(data)
                # Logging
                log_lines.append(f"File: {filename}")
                for field, value in data.items():
                    if field == 'Source File':
                        continue
                    conf = field_conf.get(field, '')
                    if value:
                        log_lines.append(f"  Extracted: {field} = {value} (Confidence: {conf})")
                    else:
                        log_lines.append(f"  Missed: {field}")
                log_lines.append("")
                print(f"Processed {filename}")
            except Exception as e:
                log_lines.append(f"Error processing {file_path}: {e}")
                print(f"Error processing {file_path}: {e}")
    # Save combined CSV
    if all_data:
        df = pd.DataFrame(all_data)
        combined_csv = os.path.join(output_dir, "combined_results.csv")
        df.to_csv(combined_csv, index=False)
        print(f"Combined results saved to {combined_csv}")
    # Save log file
    log_file = os.path.join(output_dir, f"extraction_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")
    with open(log_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(log_lines))
    print(f"Log saved to {log_file}")

if __name__ == "__main__":
    process_all_documents() 