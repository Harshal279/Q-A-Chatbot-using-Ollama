import streamlit as st 
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms.ollama import Ollama 
import os 
from dotenv import load_dotenv

load_dotenv()

os.environ['LANGSMITH_TRACING'] = "true"
os.environ['LANGSMITH_API_KEY'] = "Your_api_key"
os.environ['LANGSMITH_PROJECT'] = "Q&A Chatbot(ollama)"

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Respond to the user's queries."),
    ("human", "Question: {question}")
])

def generate_response(question, llm_model):
    llm = Ollama(model=llm_model)  
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    answer = chain.invoke({"question": question})
    return answer

# Streamlit UI
st.title("Local LLM Chatbot (Ollama)")
llm_model = st.sidebar.selectbox("Select the Model", [
    "gemma:2b", 
    "mxbai-embed-large:latest",
    "llama3.2:latest",
    "llama3:latest"
])
st.sidebar.markdown("Temperature and Max Tokens are managed by Ollama configuration.")

st.write("Go ahead and ask any question")
user_input = st.text_input("You:")

if user_input:
    response = generate_response(user_input, llm_model)
    st.write(f": {response}")
else:
    st.write("Please provide a query")
