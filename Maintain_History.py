import os 

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

llm = ChatOpenAI(model = "gpt-4o-mini" , api_key= os.getenv("OPENAI_API_KEY"))

#empty conversation list
messages = []

while True:
    user_input = input("You : ")
    if user_input.lower() == "exit":
        break;
    messages.append(HumanMessage(content = user_input))

    response = llm.invoke(messages)
    print("AI : ",response.content)
    messages.append(response)