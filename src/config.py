import os
from dotenv import load_dotenv

load_dotenv()

AZURE_ENDPOINT = os.getenv('AZURE_ENDPOINT')
AZURE_KEY = os.getenv('AZURE_KEY')

INPUT_FOLDER = 'data/input'
OUTPUT_FOLDER = 'data/output'

# Expanded German telecom terms dictionary (official terms included)
GERMAN_TERMS = {
    # General
    'All-IP-Netz': 'All IP Network',
    'Analog': 'Analog',
    'Digital': 'Digital',
    'Backbone': 'Backbone',
    'Carrier': 'Carrier',
    'Call-by-Call': 'Call-by-Call',
    'Preselection': 'Preselection',
    'Terminierungsentgelt': 'Termination Fee',
    # Broadband & Fixed Network
    'DSL': 'DSL',
    'ADSL': 'ADSL',
    'TAL': 'Local Loop',
    'Teilnehmeranschlussleitung': 'Subscriber Line',
    'Entbündelung': 'Unbundling',
    'ULL': 'Unbundled Local Loop',
    'LLU': 'Local Loop Unbundling',
    'Line-Sharing': 'Line Sharing',
    'Bitstromzugang': 'Bitstream Access',
    'Schaltverteiler': 'Main Distribution Frame',
    # Mobile & Wireless
    'Funkzelle': 'Cell',
    'Cell': 'Cell',
    'Roaming': 'Roaming',
    'National Roaming': 'National Roaming',
    'Geisterroaming': 'Phantom Roaming',
    'UMTS': 'UMTS',
    'HSPA': 'HSPA',
    'LTE': 'LTE',
    'WLAN': 'WLAN',
    # Regulation & Frequencies
    'Bundesnetzagentur': 'Federal Network Agency',
    'BNetzA': 'Federal Network Agency',
    'Frequenzzuteilung': 'Frequency Allocation',
    'Allgemeinzuteilung': 'General Allocation',
    'Einzelzuteilung': 'Individual Allocation',
    'Netzabdeckung': 'Network Coverage',
    'Versorgungsgrad': 'Coverage Level',
    'Weiße Flecken': 'White Spots',
    'NGN': 'Next Generation Network',
    # Technology
    'VoIP': 'Voice over IP',
    'IPTV': 'IPTV',
    # Glossary Table Terms
    'Schaltverteiler': 'Distribution Frame',
    'Analoge Übertragung': 'Analog Transmission',
    'Digitale Übertragung': 'Digital Transmission',
    'Funkzelle': 'Radio Cell',
    'Netzabdeckung': 'Network Coverage',
    'Weiße Flecken': 'White Spots',
    'Frequenzzuteilung': 'Frequency Allocation',
    'Terminierungsentgelt': 'Termination Fee',
    # Existing and previously added terms (equipment, specs, fields, etc.)
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
    'Leistung': 'Power',
    'Kapazität': 'Capacity',
    'Abmessungen': 'Dimensions',
    'Prüfstrom': 'Test Current',
    'max.': 'Maximum',
    'Technische Daten': 'Technical Data',
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