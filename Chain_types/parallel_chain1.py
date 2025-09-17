from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel

load_dotenv()

OPENAI_API_KEY="Paste your openai api key"


model1 = ChatOpenAI(model='gpt-4-turbo', api_key = OPENAI_API_KEY)
model2 = ChatOpenAI(model='gpt-4-turbo', api_key = OPENAI_API_KEY)

prompt1 = PromptTemplate(
    template = 'generate short and simple notes from the following text \n{text}',
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template = 'generate 5 short question answers from the following text \n{text}',
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template = 'merge the provided notes and quiz into the single document \n notes -> {notes} and quiz -> {quiz}',
    input_variables=['text']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz': prompt2 | model2 | parser
})

merge_chain = prompt3 | model1 | parser

chain = parallel_chain | merge_chain

text = """
1. Supervised Learning:
- Introduction: Supervised learning involves training a model on labeled
data, where the target variable is known.
- Learning Process: The model learns from input-output pairs to make
predictions on new, unseen data.
- Common Algorithms: Linear Regression, Decision Trees, Support
Vector Machines (SVM), Neural Networks.
2. Unsupervised Learning:
- Introduction: Unsupervised learning deals with unlabeled data, where
the model explores patterns and relationships within the data on its own.
- Learning Process: The model identifies hidden structures or clusters in
the data without any explicit guidance.
- Common Algorithms: K-Means Clustering, Hierarchical Clustering,
Principal Component Analysis (PCA).
"""

result = chain.invoke({'text':text})

print(result)


# Above code is for parallel chain 
# In this code we are used 3 prompts and 2 models for getting our output.
# In parallel chain we can excute multiple chain at same time, and we will get our desired ouput.