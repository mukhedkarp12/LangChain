import os

from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableParallel, RunnableLambda, RunnablePassthrough

double = RunnableLambda(lambda x : 2 * x)  #creating our custom Runnable method
square = RunnableLambda(lambda x : x * x)

parallel = RunnableParallel(
        original = RunnablePassthrough(),# to hold the input sent to all the parallel branches. Only 1 input will be sent to all the branches for parallel branches.
        double =  double, #here double is var name and other double is the Runnable method name
        square = square  #here also same. These are keys / branch names with which we can access the result dict using this keys
)

result = parallel.invoke(5) 
print(result["double"])
print(result["original"])
print(result["square"])
