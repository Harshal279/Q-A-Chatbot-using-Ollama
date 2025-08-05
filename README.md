# Q-A-Chatbot-using-Ollama
# Local LLM Chatbot using Ollama + LangChain + Streamlit

This project is a local chatbot web app built using **Streamlit**, **LangChain**, and **Ollama**. It enables users to interact with locally hosted large language models like **LLaMA 3**, **Gemma**, etc., directly from a clean and simple UI.

---

## 🚀 Features

- ✅ Run Local LLMs (LLaMA3, Gemma, and more)
- ✅ Simple Streamlit-based interface
- ✅ Uses LangChain for prompt handling and chaining
- ✅ Supports model switching from sidebar
- ✅ LangSmith integration for tracing and monitoring

---

## 🧠 Tech Stack

- [Streamlit](https://streamlit.io/)
- [LangChain](https://www.langchain.com/)
- [Ollama](https://ollama.com/)
- [LangSmith (optional)](https://smith.langchain.com/)

---

## 📦 Installation

### 1. Clone this repository
```bash
git clone https://github.com/your-username/ollama-streamlit-chatbot.git
cd ollama-streamlit-chatbot

---

```bash
python -m venv venv

```bash
source venv/bin/activate  # On Windows: venv\Scripts\activate

---

pip install -r requirements.txt

---

```bash
ollama pull gemma:2b
ollama pull llama3
ollama pull llama3.2:latest
ollama pull llama3:latest

