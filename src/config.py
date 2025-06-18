import os
from dotenv import load_dotenv

load_dotenv()

AZURE_ENDPOINT = os.getenv('AZURE_ENDPOINT')
AZURE_KEY = os.getenv('AZURE_KEY')

INPUT_FOLDER = 'data/input'
OUTPUT_FOLDER = 'data/output'

GERMAN_TERMS = {
    'Antennenträger': 'Antenna Support',
    'Schornstein': 'Chimney/Tower',
    'Batterieketten': 'Battery Chains',
    'Zustandskontrolle': 'Condition Inspection',
    'Mängelzusammenstellung': 'Defect Summary',
    'Plattform': 'Platform',
    'Antenne': 'Antenna',
    'Batterie': 'Battery',
    'Messung': 'Measurement',
    'Schrank': 'Cabinet',
    'Schaltanlage': 'Switchgear',
    'Lotrechtstellung': 'Vertical Alignment',
    'Beschichtungsdicken': 'Coating Thickness',
    'Schraubprüfung': 'Bolt Check',
    # Add more as needed
} 