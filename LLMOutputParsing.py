import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


key = os.getenv("OPENAI_API_KEY")  #get open AI APi key , that is set in my system variables

# now u can create llm object once u get api key to connect to the model
llm = ChatOpenAI(model = "gpt-4.1-mini", api_key= key)


# now create a prompttemplate object, This is used to format the prompt. User may not always properly 
# specifying the prompt, so we need to format the propmt before sending it to the llm

prompt_template = PromptTemplate.from_template(
        """
            Give a simple recipe for a {dish}

              Requirements:
            - List ingredients
            - Give step-by-step procedure
            - Use very simple English
        """
        )

#Get the input from the user for the dish he requires
dish = input("Which dish you would like to have today  ")

#now we invoke prompt template invoke() to format the prompt
prompt = prompt_template.invoke(
    {
    "dish" : dish
    }
)

print(prompt.text)

# now call llm invoke and pass the formatted prompt that we got from using prompt_template.invoke()
response = llm.invoke(prompt)

#pass the response ie. AI message that we got from llm.invoke to OUtparser
parser = StrOutputParser()
result = praser.invoke(response)

print("\n Recipe " )
print(result)