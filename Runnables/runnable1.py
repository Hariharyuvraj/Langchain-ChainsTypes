from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence

OPENAI_API_KEY= "Paste your openai key"

# Model creation
llm = ChatOpenAI(model="gpt-3.5-turbo", api_key=OPENAI_API_KEY)

# Prompts creation
prompt_summary = ChatPromptTemplate.from_messages([
    ('system',  "You are a helpful assistant."),
    ('human',   "Summarize this text: {text}")
])

prompt_poem = ChatPromptTemplate.from_messages([
    ('system',   "You are a poet."),
    ('human' , "Write a short poem about this summary: {summary}")
])

# Chains
summary_chain = prompt_summary | llm | StrOutputParser()

poem_chain = prompt_poem | llm | StrOutputParser()

# RunnableSequence → step by step
chain = RunnableSequence(first=summary_chain, last=poem_chain)

# Run 
response = chain.invoke({"text": "The rain falls gently, bringing peace and freshness to the earth."})
print(response)

# In this runnablesequence we can mention chain will execute first and last
# Runnable helps to execute the prompts at any way ,it provides flexibility
# if we are using 'ChatPromptTemplate' in code then we should use 'system', 'human' messages