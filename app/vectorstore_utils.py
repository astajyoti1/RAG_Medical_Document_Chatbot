from langchain_community.vectorstores import Chroma, FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from typing import List

def create_faiss_index(texts: List[str]):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return FAISS.from_texts(texts, embeddings)


def retrieve_relevant_docs(vectorstore: FAISS, query: str, k: int = 4):
    return vectorstore.similarity_search(query, k=k)