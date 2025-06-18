# Telecom Asset Extraction

## Project Overview
This project is an AI-powered system for extracting structured asset information from German telecommunications inspection documents (PDFs/images). It uses Azure Document Intelligence (Form Recognizer) to process documents and outputs a standardized CSV with telecom equipment, antennas, batteries, and infrastructure data. A web interface (Streamlit) is included for easy uploads and downloads.

---

## Features
- Batch process German telecom PDFs/images
- Extracts site IDs, equipment names, quantities, technical specs, manufacturer, serial numbers, dates, and more
- Outputs a 21-field standardized CSV
- Confidence scores for each field
- Detailed logs showing extracted vs. missed fields
- Simple web interface for uploads and downloads
- Ready for deployment on Streamlit Cloud

---

## Setup Instructions

### 1. Clone the Repository
```
git clone https://github.com/AleemBajwa/telecom.git
cd telecom
```

### 2. Create and Activate a Virtual Environment (Recommended)
```
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```
pip install -r requirements.txt
python -m spacy download de_core_news_sm
```

### 4. Set Up Azure Credentials
Create a `.env` file in the project root (do NOT commit this file):
```
AZURE_ENDPOINT=your_azure_endpoint_here
AZURE_KEY=your_azure_key_here
```

---

## Local Usage

### Batch Processing (Command Line)
1. Place your PDF/image files in `data/input/`.
2. Run:
   ```
   python src/main.py
   ```
3. Find CSV results and logs in `data/output/`.

### Generate Sample Documents
To create sample German telecom PDFs for testing:
```
python src/sample_pdf_generator.py
```

---

## Web Interface (Streamlit)
1. Run locally:
   ```
   streamlit run app.py
   ```
2. Upload documents, process, and download CSVs via the browser.

---

## Deployment (Streamlit Cloud)
1. Ensure `runtime.txt` is in the repo root with `python-3.10` or `python-3.11`.
2. Push your code to GitHub.
3. Go to [Streamlit Cloud](https://streamlit.io/cloud) and sign in with GitHub.
4. Click "New app", select your repo and branch, and set the main file to `app.py`.
5. In Advanced Settings, add your Azure credentials as secrets:
   ```
   AZURE_ENDPOINT = "your_azure_endpoint"
   AZURE_KEY = "your_azure_key"
   ```
6. Deploy and use your app online!

---

## Interpreting Logs
- After each batch run, a log file is saved in `data/output/` (e.g., `extraction_log_YYYYMMDD_HHMMSS.txt`).
- For each document, the log lists:
  - Extracted fields (with values and confidence)
  - Missed fields (empty or low confidence)
  - Any errors encountered

---

## Support & Handover
- **Repository:** [https://github.com/AleemBajwa/telecom](https://github.com/AleemBajwa/telecom)
- **Live App:** [https://telecom-dm4cqthvmmht9gs4fpmqky.streamlit.app/](https://telecom-dm4cqthvmmht9gs4fpmqky.streamlit.app/)
- **Azure Credentials:** Set these in Streamlit Cloud as described above (never commit to repo)

If you have any questions or want to extend the system, please reach out!

---

## Quick Checklist
- [ ] Virtual environment activated and working
- [ ] Azure OCR processes German text correctly
- [ ] Site IDs extracted with simple regex
- [ ] Equipment names identified in German
- [ ] CSV exports without encoding issues
- [ ] Simple web interface functional
- [ ] Deployed and accessible online
- [ ] Processing logs show what was extracted vs. missed 