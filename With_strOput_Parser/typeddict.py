from langchain_openai import ChatOpenAI
from dotenv  import load_dotenv
from typing import TypedDict

load_dotenv()

OPENAI_API_KEY="Paste your openai api key"


model = ChatOpenAI(model='gpt-4', api_key=OPENAI_API_KEY)

#schema
class Review(TypedDict):
    summary:str
    sentiment:str
structured_model = model.with_structured_output(Review)



result = structured_model.invoke("Generative AI is a powerful technology that enables machines to create human-like content, including text, images, audio, and even code. It is transforming industries by automating creative tasks, enhancing productivity, and supporting innovation. While it offers great benefits like efficiency and personalization, it also comes with challenges such as ethical concerns, bias, and misuse. Overall, Generative AI is shaping the future by blending creativity with intelligence")

print(result)
print(result['summary'])
print(result['sentiment'])

# with the help of "with_strutured_output" function in langchain by using "TypedDict" we can get o/p in our required formate.
# In this code we use "TypedDict" way to get o/p in desirable structure.

# Note: "Before the invoke model we need to give what type of o/p data formate needed."

# with structured o/p data we can easily extract required informations just like 'sentiment', 'summary' etc