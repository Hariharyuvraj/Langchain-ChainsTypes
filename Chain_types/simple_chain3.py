from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

OPENAI_API_KEY="Paste your openai api key"

model = ChatOpenAI(
    model = 'gpt-4-turbo', api_key = OPENAI_API_KEY,
    max_completion_tokens=100
)

prompt1 = PromptTemplate(
    template ='Generate detailed report on {topic}',
    input_variables = ['topic']
)

prompt2 = PromptTemplate(
    template = 'summary of {topic}',
    input_variables = ['topic']
)

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({'topic':'innovation in IT technology'})

print(result)

# By using 2 prompt we can make chain to excecute our o/p
# In our chain we use 2 prompts, i.e one is depend on other prompt
# it means after 1 prompt 2 is active and with the hepl of 'chain' it automates all operations.