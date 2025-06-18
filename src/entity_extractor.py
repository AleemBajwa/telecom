import re
import config
from typing import Tuple

def extract_site_id(text) -> Tuple[str, float]:
    # Example: DE-TIMS-\d{5,6}, \d{4}[A-Z]?, OX[LU] \d{3,4}
    patterns = [
        r'DE-TIMS-\d{5,6}',
        r'\d{4}[A-Z]?',
        r'OX[LU] \d{3,4}'
    ]
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            return match.group(), 0.95
    return '', 0.0

def extract_equipment(text) -> Tuple[str, float]:
    # Search for German equipment terms
    for term in config.GERMAN_TERMS.keys():
        if term in text:
            return term, 0.9
    return '', 0.0

def extract_quantity(text) -> Tuple[str, float]:
    # Find numbers followed by units
    match = re.search(r'(\d+)\s*(Stück|pcs|x)', text)
    if match:
        return match.group(1), 0.9
    return '', 0.0

def extract_manufacturer(text) -> Tuple[str, float]:
    match = re.search(r'Hersteller[:\s]+([A-Za-z0-9\- ]+)', text)
    if match:
        return match.group(1).strip(), 0.85
    return '', 0.0

def extract_serial_number(text) -> Tuple[str, float]:
    match = re.search(r'Seriennummer[:\s]+([A-Za-z0-9\-]+)', text)
    if match:
        return match.group(1).strip(), 0.85
    return '', 0.0

def extract_power(text) -> Tuple[str, float]:
    match = re.search(r'(\d+[\.,]?\d*)\s*(kW|W)', text)
    if match:
        return match.group(0), 0.9
    return '', 0.0

def extract_capacity(text) -> Tuple[str, float]:
    match = re.search(r'(\d+[\.,]?\d*)\s*Ah', text)
    if match:
        return match.group(0), 0.9
    return '', 0.0

def extract_dimensions(text) -> Tuple[str, float]:
    match = re.search(r'(\d+\s*[xX]\s*\d+\s*[xX]\s*\d+\s*(mm|cm|m))', text)
    if match:
        return match.group(1), 0.9
    return '', 0.0

def extract_date(text) -> Tuple[str, float]:
    match = re.search(r'(\d{2}\.\d{2}\.\d{4})', text)
    if match:
        return match.group(1), 0.95
    return '', 0.0

def extract_field(text, field):
    # Placeholder for unmapped fields
    return '', 0.0 