from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 1. lets make LLM 

OPENAI_API_KEY="Paste your openai api key"

model = ChatOpenAI(model='gpt-4', api_key=OPENAI_API_KEY)

# 2. Prompt Template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "Write a short poem about {topic}.")
])

# 3. Output Parser gives our output in 'str' formate 
parser = StrOutputParser()

# 4. we can make Chain formation like this
chain = prompt | model | parser

# 5. can run the code
response = chain.invoke({"topic": "sun"})
print(response)


# In this code we use 1 prompt to convert the o/p with help of 'str_output_parser'
# we make 'chain' in this code. 