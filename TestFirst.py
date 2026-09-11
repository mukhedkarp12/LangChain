import os
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI

# Get the API key , from system environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") #function

#create CahtOpenAI object, by passing the key and model name we are using
llm = ChatOpenAI(model="gpt-4o",api_key=OPENAI_API_KEY)

#set the human message
human_message = HumanMessage(content = "Hello, My Name is Pratibha  Mukhedkar")

#get the response from AI , return type of invoke is AIMessage
ai_message = llm.invoke("Hello My Name is Pratibha Mukhedkar")
print(ai_message.content)

#ow we re checking if my AI is remembering me or not
#checking for context/ memory of AI
ai_message = llm.invoke("Oh wonderful LLM, What is my Name:")
print(ai_message.content)
# But llm does not have the capacity to remember me. It does not have the context and does not store 
# anything