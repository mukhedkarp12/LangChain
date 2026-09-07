import os
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(model = "gpt_4o_mini"  , api_key = "OPENAI_API_KEY")


prompt_template = PromptTemplate.from_template(
    "Explain {topic} in simple English at  {level} level  ",
     partial_variables = {
        "topic" : "Python", 
        "level" : "Beginner"
    }
)


prompt_value = prompt_template.invoke(
    {
        "topic" : "Java",
        #"level" : "Advanced"
    }
)

print(prompt_template)
print()
print()
print()
print(prompt_value.to_string())