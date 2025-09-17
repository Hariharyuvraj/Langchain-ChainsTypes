from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

OPENAI_API_KEY="Paste your openai api key"

prompt = PromptTemplate(
    template = 'Generate 5 interesting facts about {topic}',
    input_variable = ['topic']
)

model = ChatOpenAI(model = 'gpt-4-turbo', api_key=OPENAI_API_KEY)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({'topic':'goal setting'})

print(result)