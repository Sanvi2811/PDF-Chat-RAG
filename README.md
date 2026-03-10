# 📄 RAG PDF Assistant

A **Retrieval-Augmented Generation (RAG) based PDF Question Answering System** that allows users to upload a PDF document and ask questions about its contents.  
The system processes the document, creates vector embeddings, retrieves relevant information, and generates answers using a language model.

---

## 🚀 Features

- 📄 Upload any PDF document
- 🧠 Ask questions related to the PDF content
- 🔎 Semantic search using vector embeddings
- ⚡ Fast retrieval using FAISS vector database
- 💬 Interactive chat interface
- 🌐 FastAPI backend with a simple web frontend

---

## 🛠 Tech Stack

### Frontend
- HTML
- CSS
- JavaScript

### Backend
- Python
- FastAPI
- Uvicorn

### AI / RAG Components
- LangChain
- FAISS Vector Database
- Azure OpenAI Embeddings
- Ollama (LLaMA2)

### Other Libraries
- PyPDFLoader
- RecursiveCharacterTextSplitter

---

## 📁 Project Structure
RAG_PROJECT
│
├── frontend.html # Web interface for uploading PDF and asking questions
├── main.py # FastAPI backend server
├── rag.py # RAG pipeline logic
├── .env # Environment variables (API keys)
└── README.md # Project documentation

---

## ⚙️ How It Works

1️⃣ **PDF Upload**  
User uploads a PDF file from the web interface.

2️⃣ **Document Processing**  
- The PDF is loaded using `PyPDFLoader`
- Text is split into chunks using `RecursiveCharacterTextSplitter`

3️⃣ **Embedding Generation**  
Each chunk is converted into vector embeddings using **Azure OpenAI Embeddings**.

4️⃣ **Vector Storage**  
Embeddings are stored in a **FAISS vector database**.

5️⃣ **Question Answering**  
- User asks a question
- Relevant chunks are retrieved
- Context is passed to the LLM
- The model generates a contextual answer.

---

## 🧑‍💻 Installation

### 1️⃣ Clone the Repository
git clone https://github.com/yourusername/rag-pdf-assistant.git
cd rag-pdf-assistant

###2️⃣ Create Virtual Environment
python -m venv venv
Activate the environment.
Windows

venv\Scripts\activate

Mac/Linux

source venv/bin/activate
3️⃣ Install Dependencies
pip install fastapi uvicorn langchain langchain-community langchain-openai faiss-cpu pypdf
4️⃣ Configure Environment Variables

Create a .env file and add:
AZURE_OPENAI_API_KEY=your_api_key
AZURE_OPENAI_ENDPOINT=your_endpoint
AZURE_OPENAI_API_VERSION=your_api_version
AZURE_OPENAI_EMBEDDING_DEPLOYMENT=your_embedding_deployment
5️⃣ Install and Run Ollama
Install Ollama and pull the LLaMA2 model:

ollama pull llama2
▶️ Running the Application

Start the FastAPI backend server:

python main.py

The server will run at:

http://localhost:8000
🌐 Open the Frontend

Open the following file in your browser:

frontend.html
💬 Usage

Upload a PDF document

Wait for processing

Ask questions related to the document

Get AI-generated answers based on the document content

🔮 Future Improvements

Multi-PDF support

Persistent vector database

Improved UI/UX

Streaming responses

Docker deployment

Authentication system

👩‍💻 Author

Sanvi Tripathi

Engineering Student interested in:

Artificial Intelligence

Machine Learning

Intelligent Systems
