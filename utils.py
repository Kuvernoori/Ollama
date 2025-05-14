import os
import json
from langchain.llms import Ollama
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import TextLoader, PyMuPDFLoader, Docx2txtLoader

def get_llm():
    return Ollama(model="mistral")

def get_embeddings():
    return HuggingFaceEmbeddings()

def split_documents(docs):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    return splitter.split_documents(docs)

def load_constitution_to_vectorstore():
    loader = TextLoader("constitution.txt")
    documents = loader.load()
    docs = split_documents(documents)
    embeddings = get_embeddings()
    vectorstore = Chroma.from_documents(docs, embedding=embeddings, persist_directory="chroma_db")
    vectorstore.persist()
    return vectorstore

def process_uploaded_files(uploaded_files):
    os.makedirs("data", exist_ok=True)
    docs = []
    for file in uploaded_files:
        file_path = os.path.join("data", file.name)
        with open(file_path, "wb") as f:
            f.write(file.getbuffer())
        if file.name.endswith(".pdf"):
            loader = PyMuPDFLoader(file_path)
        elif file.name.endswith(".docx"):
            loader = Docx2txtLoader(file_path)
        else:
            continue
        docs.extend(loader.load())
    return docs

def save_interaction(query, answer):
    with open("chat_log.json", "a", encoding="utf-8") as f:
        f.write(json.dumps({"query": query, "answer": answer}, ensure_ascii=False) + "\n")
