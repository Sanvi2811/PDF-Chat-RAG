from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import AzureOpenAIEmbeddings
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama

# Globals to persist between queries
retrieval_chain = None

def process_pdf(file_path):
    global retrieval_chain
    
    # 1. Load PDF
    loader = PyPDFLoader(file_path)
    documents = loader.load()

    # 2. Chunk
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = text_splitter.split_documents(documents)

    # 3. Embeddings + FAISS
    embeddings = AzureOpenAIEmbeddings(
        deployment=os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT"),
        model="text-embedding-ada-002",
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        api_version=os.getenv("AZURE_OPENAI_API_VERSION")
    )
    db = FAISS.from_documents(docs, embedding=embeddings)

    # 4. Retriever
    retriever = db.as_retriever()

    # 5. LLM + Prompt + Chain
    llm = Ollama(model="llama2")
    prompt = ChatPromptTemplate.from_template("""
    You are a knowledgeable assistant that answers questions strictly using the information from the provided database context. 
    If the answer is not found in the context, say "I could not find that information in the database."
    <context>
    Context:
    {context}
    </context>
    Question:{input}
    Answer in a clear and concise way:""")
    
    documents_chain = create_stuff_documents_chain(llm, prompt)
    retrieval_chain = create_retrieval_chain(retriever, documents_chain)
    return "PDF processed successfully!"
    

def ask_question(query: str):
    global retrieval_chain
    if retrieval_chain is None:
        return "Please upload a PDF first."
    response = retrieval_chain.invoke({"input": query})
    return response["answer"]
