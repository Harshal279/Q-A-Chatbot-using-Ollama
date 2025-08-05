# 🤖 Q-A Chatbot using Ollama

Q-A Chatbot using Ollama is a lightweight and powerful web-based chatbot interface that leverages **local large language models (LLMs)** with the help of **LangChain**, **Streamlit**, and **Ollama**. It allows users to interact with multiple local models in a conversational format through a clean and intuitive UI.

---

## 🚀 Features

### 🔐 Authentication & Setup
- Uses `.env` for secure API key injection
- LangSmith tracing support for debugging and monitoring

### 🧠 LLM Support (via Ollama)
- gemma:2b
- llama3
- llama3:latest
- llama3.2:latest
- mxbai-embed-large:latest

### 🗣️ Prompt Handling & Response
- LangChain-powered prompt chaining
- Custom prompt template for consistent AI behavior
- Streaming response capability (can be extended)

### 💻 Streamlit Web Interface
- User input for questions
- Model selection from sidebar
- Interactive Q&A output area

---

## 🛠️ Tech Stack

### 🔧 Backend
- **LangChain** – For chaining prompts and model interaction
- **Ollama** – Running local LLMs
- **Python** – Core application logic
- **dotenv** – Environment variable support

### 💻 Frontend
- **Streamlit** – Lightweight web frontend for user interaction

---

## 📦 Installation

### ✅ Prerequisites
- Python 3.8+
- Ollama installed and running locally
- Models downloaded via `ollama pull`
- Docker (optional, if containerizing)

### 🧰 Setup Instructions

```bash
# 1. Clone the repository
git clone https://github.com/your-username/Q-A-Chatbot-using-Ollama.git
cd Q-A-Chatbot-using-Ollama

# 2. Create virtual environment
python -m venv venv

# 3. Activate the environment
# On Windows:
venv\Scripts\activate

# 4. Install dependencies
pip install -r requirements.txt

