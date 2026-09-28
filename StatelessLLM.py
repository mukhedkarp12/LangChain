import os

# this program tells us that 2 invokes are nowhere realted to each other. They are 2 independent calls and 
# does not remeber previous msgs/ history which is nothing but the stateless behaviour of AI models.

from langchain_openai import ChatOpenAI

model = ChatOpenAI(model = 'gpt-4o-mini', api_key = os.getenv('OPENAI_API_KEY'))

# here the llm call gets 1st msg 
response1 = model.invoke("My name is Pratibha m")
print(response1.content)

# llm is invoked with 2nd msg only. No history is send to llm. Only STRING msg sent, so llm would reply saying 
# i cant access your details, i dont know you etc...
response2 = model.invoke("what is my name?? ")
print(response2.content)


# with conversation history

messages = [
        HumanMessage(content = "My name is pratibha"),
        AIMessage(content = "great Pratibha how can i help you"),
        HumanMessage(content = "What is my name")
]

response = llm.invoke(messages)