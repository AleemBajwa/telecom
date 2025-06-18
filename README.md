# Telecom Asset Extraction

This project extracts structured asset information from German telecom inspection documents (PDFs/images) using AI-powered OCR and entity extraction.

## Project Structure

- `data/input/`   - Place your PDF/image files here
- `data/output/`  - Extracted CSV results will go here
- `src/`          - Source code for processing, extraction, and CSV generation

## Quick Start
1. Place documents in `data/input/`
2. Run the main processing script in `src/`
3. Find results in `data/output/`

## Main Components
- OCR processing (Azure Form Recognizer)
- Entity extraction (regex, German terms)
- CSV export

## Web Interface

You can use the Streamlit app for easy uploads and CSV downloads:

```sh
streamlit run app.py
```

## Deployment (Streamlit Cloud)
1. Push your code to GitHub.
2. Go to https://streamlit.io/cloud and connect your repo.
3. Set environment variables (`AZURE_ENDPOINT`, `AZURE_KEY`) in the Streamlit Cloud dashboard.
4. Deploy!

---

This file will be updated as the project progresses. 