import re
from src import config
from typing import Tuple

def extract_site_id(text) -> Tuple[str, float]:
    # Try to find a 4-digit or 5-digit number at the start (site code)
    match = re.search(r'\b\d{4,5}\b', text)
    if match:
        return match.group(), 0.95
    # Fallback to previous patterns
    patterns = [
        r'DE-TIMS-\d{5,6}',
        r'\d{4}[A-Z]?',
        r'OX[LU] \d{3,4}'
    ]
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            return match.group(), 0.9
    return '', 0.0

def extract_equipment(text) -> Tuple[str, float]:
    # Look for known equipment names in the text
    equipment_keywords = [
        'DOPHENIX', 'POWERTRAB', 'Powerset', 'Rita Rack', 'Rifa Rack',
        'Systemerde', 'Brücke', 'Tür'
    ] + list(config.GERMAN_TERMS.keys())
    for eq in equipment_keywords:
        if eq.lower() in text.lower():
            return eq, 0.9  # Return only the first match
    return '', 0.0

def extract_quantity(text) -> Tuple[str, float]:
    match = re.search(r'(\d+)\s*(Stück|pcs|x)', text)
    if match:
        return match.group(1), 0.9
    # Try to extract numbers after 'max.'
    match = re.search(r'max\.\s*([\d]+[×xX][\d]+)', text)
    if match:
        return match.group(1), 0.8
    return '', 0.0

def extract_manufacturer(text) -> Tuple[str, float]:
    # Try to find manufacturer by known names or patterns
    match = re.search(r'(DOPHENIX|POWERTRAB|Powerset|Bosch|Siemens|ABB|Rittal)', text, re.IGNORECASE)
    if match:
        return match.group(1), 0.85
    return '', 0.0

def extract_serial_number(text) -> Tuple[str, float]:
    # Look for Best.Nr. followed by numbers
    match = re.search(r'Best\.Nr\.?\s*([\d]+)', text)
    if match:
        return match.group(1), 0.95
    # Also try SN- pattern
    match = re.search(r'SN-([\d]+)', text)
    if match:
        return match.group(1), 0.85
    return '', 0.0

def extract_power(text) -> Tuple[str, float]:
    match = re.search(r'(\d+[\.,]?\d*)\s*(kW|W)', text)
    if match:
        return match.group(0), 0.9
    # Try to extract from 'Prufstrom' or 'Test Current'
    match = re.search(r'Prufstrom[:\s]*([\d]+\s*KA)', text, re.IGNORECASE)
    if match:
        return match.group(1), 0.8
    return '', 0.0

def extract_capacity(text) -> Tuple[str, float]:
    match = re.search(r'(\d+[\.,]?\d*)\s*Ah', text)
    if match:
        return match.group(0), 0.9
    # Try to extract from 'max.'
    match = re.search(r'max\.\s*([\d]+[×xX][\d]+)', text)
    if match:
        return match.group(1), 0.8
    return '', 0.0

def extract_dimensions(text) -> Tuple[str, float]:
    match = re.search(r'(\d+\s*[xX×]\s*\d+\s*[xX×]\s*\d+\s*(mm|cm|m))', text)
    if match:
        return match.group(1), 0.9
    return '', 0.0

def extract_date(text) -> Tuple[str, float]:
    match = re.search(r'(\d{2}\.\d{2}\.\d{4})', text)
    if match:
        return match.group(1), 0.95
    return '', 0.0

def extract_field(text, field):
    # Extract technical data for 'Notes' or 'Technical Data' fields
    if field.lower() in ['notes', 'technical data', 'technische daten']:
        match = re.search(r'Technische Daten[\s:]*([\w\W]+?)(?:\n|$)', text)
        if match:
            return match.group(1).strip(), 0.9
    # For 'Rack Info', extract all rack-related lines
    if 'rack' in field.lower():
        racks = re.findall(r'(Rita Rack \d+|Rifa Rack \d+)', text, re.IGNORECASE)
        if racks:
            return "; ".join(racks), 0.9
    # For 'Grounding', extract 'Systemerde' or similar
    if 'ground' in field.lower() or 'erde' in field.lower():
        match = re.search(r'Systemerde', text, re.IGNORECASE)
        if match:
            return match.group(0), 0.9
    return '', 0.0

# Catch-all for unmapped but recognized terms

def extract_detected_terms(text) -> Tuple[str, float]:
    detected = []
    for term in config.GERMAN_TERMS.keys():
        if term.lower() in text.lower():
            detected.append(term)
    if detected:
        return "; ".join(sorted(set(detected))), 0.7
    return '', 0.0 