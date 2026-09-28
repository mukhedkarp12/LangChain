import os

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

#Create chat model
llm = ChatOpenAI(model = "gpt-4o-mini", api_key = os.getenv("OPENAI_API_KEY"))

#Step 1: First user message
first_message = HumanMessage(content = "My name is Durga")

response1 = llm.invoke(
    [first_message]
    )

print(response1.content)

#Step 2 : New call without history
question = HumanMessage(
    content = """What is my name?

    If you dont have data, say i dont know
    """
)
response = question.invoke([question])


#Step 3 : New call with history
messages = [first_message,response1, question] #adding all the previous msgs to the list 
response3 = llm.invoke(messages)
print(response3.content)