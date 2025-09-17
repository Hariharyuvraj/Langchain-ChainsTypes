from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence

load_dotenv()

OPENAI_API_KEY= "Paste your openai api key"

model = ChatOpenAI(model = 'gpt-4-turbo', api_key = OPENAI_API_KEY)

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template = 'summerize this text in 1 line\n{text}',
    input_variables =['text']
)

prompt2 = PromptTemplate(
    template = 'Translate this into simple hindi words\n{summary}',
    input_variable = ['summary']
)

summary_chain = prompt1|model|parser
translation_chain = prompt2|model|parser

chain = RunnableSequence(
    first = summary_chain,
    last = translation_chain
)

result = chain.invoke({'text':"""Artificial Intelligence helps machines think and learn like humans,it helps to do task better accuracy and faster than humans"""})
print(result)

# in this code we use 'Runnable' function for executing the task/prompts 