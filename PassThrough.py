# This is the program , where we are creating a sequential workflow and then running those sequence in parallely.
# We have also used Runnable lambda for converting the outout from the parser which is string to the RunnableParallel
# expected input i.e Dict

import os
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

# model config
model = ChatOpenAI(
        model = "gpt-4o-mini" ,
        api_key = os.getenv("OPENAI_API_KEY"))

parser = StrOutputParser()


#explaination prompt
explaination_prompt = PromptTemplate.from_template(
    """
    Explain {topic} for {audience}

    Requirements:
    Explain in simple english
    Explain in 5 important points
    Give real time example

    """
     )

 #create explaination chain
explaination_chain = explaination_prompt | model | parser

#prepare parallel input
parallel_input = RunnableLambda(
            lambda explaination : {
                "content" : explaination
            }
)

#Summary Prompt
summary_Prompt = PromptTemplate.from_template(
    """
    Summarize 5 bullet points on the given {content}
    """
)

summary_chain = summary_Prompt | model | parser

#Quiz prompt
quiz_Prompt = PromptTemplate.from_template(
    """
      Provide 5 quiz questions based on the given content {content} 
      Give options and correct answers also
    """
)

quiz_chain = quiz_Prompt | model | parser

#social media post prompt
social_Prompt = PromptTemplate.from_template(
    """
    Create a short social post on the {content}
    """
)

social_chain = social_Prompt | model | parser

parallel_executor = RunnableParallel(
    summary = summary_chain,
    quiz = quiz_chain,
    social = social_chain,
    original_explanation = RunnablePassthrough()
)

final_chain = explaination_chain | parallel_input |  parallel_executor

topic = input("Enter the topic")
audience = input("Enter the audience")

result = final_chain.invoke({"topic" : topic, "audience" : audience})

# Original explanation
print(result["original_explanation"]["content"]) #original explantion internally contains dict objct and er accessing that
# that object by using key = "content"

#Summary
print(result["summary"])

#quiz
print(result["quiz"])