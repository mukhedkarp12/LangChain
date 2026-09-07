import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

OPENAI_API_KEY  = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(model = "gpt-4o-mini", api_key = OPENAI_API_KEY)

prompt_template= PromptTemplate.from_template("Explain {topic} in simple English ")
topic = input("Enter topic   ")
result = prompt_template.invoke(
    {
        "topic" : topic
    }
)

print(result)
print(prompt_template)


#ai_message = llm.invoke()
#print(ai_message.content)