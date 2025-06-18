from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os

# Always use the project root as base
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INPUT_DIR = os.path.join(BASE_DIR, "data", "input")
os.makedirs(INPUT_DIR, exist_ok=True)
OUTPUT_PATH = os.path.join(INPUT_DIR, "test_document.pdf")

def create_sample_pdf(output_path):
    c = canvas.Canvas(output_path, pagesize=A4)
    c.setFont("Helvetica", 12)
    lines = [
        "DE-TIMS-123456",
        "Antennenträger: Hauptmast",
        "Batterieketten: 4 Stück",
        "Hersteller: Siemens",
        "Seriennummer: SN-987654321",
        "Leistung: 2.5 kW",
        "Kapazität: 120 Ah",
        "Abmessungen: 200 x 50 x 40 cm",
        "Installationsdatum: 15.03.2023",
        "Inspektionsdatum: 20.04.2024",
        "Status: Aktiv",
        "Plattform: Dach",
        "Antenne: Typ X",
        "Batterie: Typ Y",
        "Zustandskontrolle: OK",
        "Mängelzusammenstellung: Keine",
        "Prüfer: Max Mustermann",
        "Notizen: Keine Auffälligkeiten."
    ]
    y = 800
    for line in lines:
        c.drawString(50, y, line)
        y -= 30
    c.save()

if __name__ == "__main__":
    create_sample_pdf(OUTPUT_PATH) 