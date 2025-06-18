import pandas as pd
from src import config
from src.entity_extractor import extract_detected_terms

def save_to_csv(data, output_file):
    # Define the new standardized fields as per user-provided columns
    output_fields = [
        'TIMS Site Code', 'Field Asset Name', 'Category', 'Sub-Category', 'Available Type', 'Available Sub Type',
        'Quantity', 'Status', 'Install Date', 'Serial', 'Manufacturer (Item)', 'Supplier (Item)', 'Item Number',
        'Power Capacity [kW]', 'Battery Capacity [Ah]', 'Item Cooling Capacity [Watt]', 'Height', 'Weight', 'Width', 'Depth', 'Asset Owner'
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