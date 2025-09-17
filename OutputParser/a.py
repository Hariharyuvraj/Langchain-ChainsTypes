from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 1. Model initialize

OPENAI_API_KEY="Paste your openai api key"

llm = ChatOpenAI(model="gpt-3.5-turbo", api_key="OPENAI_API_KEY")

# 2. Prompt तयार करा
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "Write a short poem about {topic}.")
])

# 3. Parser initialize
parser = StrOutputParser()

# 4. Chain तयार
chain = prompt | llm | parser

# 5. User कडून topic input घ्या
user_topic = input("Enter the topic for your poem: ")

# 6. Chain invoke करा
response = chain.invoke({"topic": user_topic})

# 7. Output print करा
print("\n--- Your Poem ---")
print(response)
