from typing import Union
from io import BytesIO
from .document_processor import DocumentProcessor

def extract_text_from_file(file: BytesIO, file_type: str) -> str:
    """
    Extracts text from various document formats.

    Args:
        file (BytesIO): A BytesIO object containing the file data.
        file_type (str): The type of file (pdf, docx, pptx, xlsx, csv, txt)
                        
    Returns:
        str: The extracted text from the document.
    """
    processor = DocumentProcessor()
    return processor.extract_text(file, file_type)