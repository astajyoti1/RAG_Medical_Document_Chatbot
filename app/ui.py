import streamlit as st

def pdf_uploader():
    return st.file_uploader(
        "Upload your medical documents", 
        type=["pdf", "docx", "pptx", "xlsx", "csv", "txt"], 
        accept_multiple_files=True,
        help="Upload one or more medical documents to extract text from them."
    )