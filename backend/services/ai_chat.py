import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

chat_model = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=GEMINI_API_KEY)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a compassionate AI therapist."),
    ("human", "{message}")
])

def get_ai_response(message):
    chain = prompt | chat_model
    response = chain.invoke({"message": message})
    return response.content
