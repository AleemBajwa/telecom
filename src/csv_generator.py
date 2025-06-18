import pandas as pd
from src import config

def save_to_csv(data, output_file):
    # Define the 21 standardized fields
    output_fields = [
        'TIMS Site Code', 'Field Asset Name', 'Category', 'Quantity',
        'Manufacturer', 'Serial Number', 'Power (kW)', 'Capacity (Ah)',
        'Dimensions (mm)', 'Installation Date', 'Inspection Date',
        'Status', 'Location', 'Platform', 'Antenna Type', 'Battery Type',
        'Certification', 'Inspector', 'Notes', 'Confidence', 'Source File'
    ]
    # Fill missing fields with empty string
    row = {field: data.get(field, '') for field in output_fields}
    # Add confidence scores for each field (if provided)
    for field in output_fields:
        conf_field = f'{field} Confidence'
        if conf_field in data:
            row[conf_field] = data[conf_field]
    df = pd.DataFrame([row])
    df.to_csv(output_file, index=False) 