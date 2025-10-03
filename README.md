# MediChatPro 🏥

MediChatPro is an intelligent medical document chat application that leverages RAG (Retrieval Augmented Generation) technology to provide accurate and context-aware responses to medical queries based on uploaded medical documents.

## Features 🌟

- **Document Processing**: Upload and process medical history documents in PDF format
- **Intelligent Chat Interface**: Interactive chat interface for querying medical information
- **RAG Technology**: Uses advanced retrieval-augmented generation for accurate responses
- **PDF Text Extraction**: Efficient extraction of text from medical PDFs
- **Vector Store Integration**: Sophisticated document embedding and retrieval system
- **User-Friendly UI**: Built with Streamlit for a seamless user experience

## Tech Stack 💻

- **Python**: Core programming language
- **Streamlit**: Web application framework
- **LangChain**: For RAG implementation and document processing
- **FAISS**: Vector store for efficient similarity search
- **PyPDF2**: PDF document processing
- **Sentence Transformers**: Document embedding generation
- **EuriAI**: Language model integration

## Project Structure 📁

```
medichatpro/
├── app/
│   ├── __init__.py
│   ├── chat_utils.py      # Chat functionality implementation
│   ├── config.py          # Configuration settings
│   ├── pdf_utils.py       # PDF processing utilities
│   ├── ui.py             # User interface components
│   └── vectorstore_utils.py # Vector store operations
├── sample_data/           # Sample medical documents
│   └── medical_history_*.pdf
├── main.py               # Application entry point
└── requirements.txt      # Project dependencies
```

## Installation 🚀

1. Clone the repository:
```bash
git clone https://github.com/yourusername/medichatpro.git
cd medichatpro
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage 🔧

1. Start the application:
```bash
streamlit run main.py
```

2. Upload medical documents through the web interface

3. Start chatting and querying your medical documents

## Features in Detail 📋

- **Document Upload**: Support for PDF medical documents
- **Text Extraction**: Automated extraction of medical information
- **Vector Embedding**: Conversion of medical text into vector representations
- **Semantic Search**: Advanced search capabilities for relevant medical information
- **Contextual Responses**: AI-generated responses based on document context
- **User Interface**: Clean and intuitive interface for document management and chat

## Configuration ⚙️

Configure the application by modifying `app/config.py`:
- API keys for language models
- Vector store settings
- Document processing parameters

## Security 🔒

- Handles medical documents with privacy in mind
- Local document processing
- Secure API integrations

## Contributing 🤝

Contributions are welcome! Please feel free to submit a Pull Request.

## License 📄

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments 👏

- Thanks to the LangChain community
- Streamlit for the amazing web framework
- FAISS for vector search capabilities
- EuriAI for language model support

---

Created with ❤️ for medical document management and analysis