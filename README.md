 AI Assistant – Constitution of Kazakhstan

 🧠 Project Objective:
The goal of this project is to build a web-based AI assistant that allows users to interact with the text of the Constitution of the Republic of Kazakhstan and any uploaded documents. The assistant uses a locally running language model (via Ollama) to answer user questions accurately and contextually.

⚙️ Technologies Used:
Technology	Purpose
Streamlit	Web interface for interaction in the browser
Langchain	LLM orchestration and document QA pipeline
Ollama	Local LLM (e.g., Mistral, Llama3) for private inference
FAISS	Vector store for semantic search of document content
Python	Core programming language


📂 File Structure:

/aistate

├── constitution.txt              
├── main.py                        
├── utils.py                      
├── vectorstore/                   
✅ Key Features:
Fully offline/local LLM execution (via Ollama)


## 🚀 How to Run This Project Locally

### 📋 Prerequisites

Make sure you have the following installed:

- Python 3.11+
- Git
- Ollama
- pip

### 🛠️ Setup Instructions

1. **Clone the repository:**

```bash
git clone https://github.com/Kuvernoori/Ollama.git
cd Ollama
pip install -r requirements.txt
ollama pull llama3
python -m streamlit run main.py
```

