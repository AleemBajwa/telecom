import config
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential

def process_document(file_path):
    """
    Process a PDF/image file using Azure OCR and return extracted text/tables.
    """
    client = DocumentAnalysisClient(
        endpoint=config.AZURE_ENDPOINT,
        credential=AzureKeyCredential(config.AZURE_KEY)
    )
    with open(file_path, 'rb') as f:
        poller = client.begin_analyze_document('prebuilt-read', document=f)
        result = poller.result()
    # Return raw text for now; further processing will be added later
    return result.content if hasattr(result, 'content') else str(result) 