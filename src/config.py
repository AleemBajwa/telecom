import os
from dotenv import load_dotenv

load_dotenv()

AZURE_ENDPOINT = os.getenv('AZURE_ENDPOINT')
AZURE_KEY = os.getenv('AZURE_KEY')

INPUT_FOLDER = 'data/input'
OUTPUT_FOLDER = 'data/output'

# Expanded German telecom terms dictionary
GERMAN_TERMS = {
    # Equipment
    'Antennenträger': 'Antenna Support',
    'Schornstein': 'Chimney/Tower',
    'Batterieketten': 'Battery Chains',
    'Plattform': 'Platform',
    'Antenne': 'Antenna',
    'Batterie': 'Battery',
    'Schrank': 'Cabinet',
    'Schaltanlage': 'Switchgear',
    'Verteiler': 'Distributor',
    'Leitung': 'Line/Cable',
    'Erdung': 'Grounding',
    'Systemerde': 'System Ground',
    'Brücke': 'Bridge',
    'Tür': 'Door',
    'Powerset': 'Power Set',
    'Rita Rack': 'Rack',
    'Rifa Rack': 'Rack',
    'DOPHENIX': 'Surge Arrester',
    'POWERTRAB': 'Surge Arrester',
    'Rittal': 'Cabinet',
    'ABB': 'Manufacturer',
    'Siemens': 'Manufacturer',
    'Bosch': 'Manufacturer',
    # Technical specs
    'Leistung': 'Power',
    'Kapazität': 'Capacity',
    'Abmessungen': 'Dimensions',
    'Prüfstrom': 'Test Current',
    'max.': 'Maximum',
    'Technische Daten': 'Technical Data',
    # Document fields
    'Hersteller': 'Manufacturer',
    'Seriennummer': 'Serial Number',
    'Best.Nr.': 'Order Number',
    'Installationsdatum': 'Installation Date',
    'Inspektionsdatum': 'Inspection Date',
    'Status': 'Status',
    'Mängelzusammenstellung': 'Defect Summary',
    'Zustandskontrolle': 'Condition Inspection',
    'Prüfer': 'Inspector',
    'Notizen': 'Notes',
    'Funktionstest': 'Function Test',
    'Defektanzeige': 'Defect Indicator',
    'Baustein': 'Module',
    'Austausch': 'Replacement',
    'Rack': 'Rack',
    'Kabel': 'Cable',
    'Erdungsschiene': 'Grounding Bar',
    'Messung': 'Measurement',
    'Schutz': 'Protection',
    'Schutzleiter': 'Protective Conductor',
    'Verbindung': 'Connection',
    'Klemme': 'Terminal',
    'Anschluss': 'Connection',
    'Baugruppe': 'Assembly',
    'Bauart': 'Type',
    'Betriebsart': 'Operating Mode',
    'Betriebsspannung': 'Operating Voltage',
    'Betriebsstrom': 'Operating Current',
    'Betriebstemperatur': 'Operating Temperature',
    'Schaltplan': 'Circuit Diagram',
    'Stromlaufplan': 'Wiring Diagram',
    'Typenschild': 'Nameplate',
    'Kennzeichnung': 'Labeling',
    'Lageplan': 'Site Plan',
    'Standort': 'Location',
    'Bauort': 'Construction Site',
    'Bauherr': 'Client',
    'Projekt': 'Project',
    'Ticket': 'Ticket',
    'Relais': 'Relay',
    'Fotodoku': 'Photo Documentation',
    # Add more as needed for your use case
} 