import os

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

llm = ChatOpenAI(model = "gpt-4o-mini", api_key = "OPENAI_API_KEY")

#empty conversation history list
messages= []

#user input
user_input = "My name is Durga"

#add messages to the list of messages
messages.append(HumanMessage(content = user_input))

response = llm.invoke(messages)
print(response.content)

#adding the AI response to the list
messages.append(response)

print(messages)
