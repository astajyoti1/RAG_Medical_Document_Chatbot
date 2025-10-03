from PyPDF2 import PdfReader
from typing import List, Optional
from io import BytesIO

def extract_text_from_pdf(file):
    """
    Extracts text from a PDF file.

    Args:
        file (BytesIO): A BytesIO object containing the PDF file data. 
                            This is typically obtained from an uploaded file in a web application.  
    Returns:
        List[str]: A list of strings, each representing the text from a page in the PDF.
    """
    reader = PdfReader(file)
    texts = ' '
    for page in reader.pages:
        text = texts + page.extract_text() or ''    
    return text