import streamlit as st
from utils import get_llm, load_constitution_to_vectorstore, get_embeddings, split_documents, process_uploaded_files, save_interaction
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA

st.set_page_config(page_title="Kazakhstan Constitution AI Assistant", layout="wide")
st.title("📜 AI Assistant: Constitution of Kazakhstan (Ollama)")

# Загружаем модель
llm = get_llm()

# Загружаем векторное хранилище
vectorstore = Chroma(persist_directory="chroma_db", embedding_function=get_embeddings())
qa = RetrievalQA.from_chain_type(llm=llm, retriever=vectorstore.as_retriever())

# Сайдбар для загрузки документов
st.sidebar.header("📎 Upload your files")
uploaded_files = st.sidebar.file_uploader("Choose .pdf or .docx files", type=["pdf", "docx"], accept_multiple_files=True)

if uploaded_files:
    docs = process_uploaded_files(uploaded_files)
    docs_split = split_documents(docs)
    vectorstore.add_documents(docs_split)
    st.sidebar.success("✅ Documents added to knowledge base.")

# Ввод вопроса
query = st.text_input("🔍 Ask a question about the Constitution or uploaded documents:")

if query:
    with st.spinner("Thinking..."):
        result = qa.run(query)
        st.write("📌 **Answer:**")
        st.success(result)
        save_interaction(query, result)
