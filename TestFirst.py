import os
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") #function
llm = ChatOpenAI(model="gpt-4o",api_key=OPENAI_API_KEY)
human_message = HumanMessage(content = "Hello, My Name is Pratibha  Mukhedkar")
ai_message = llm.invoke("Hello My Name is Pratibha Mukhedkar")
print(ai_message.content)
ai_message = llm.invoke("Oh wonderful LLM, What is my Name:")
print(ai_message.content)