import json
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

f = open('section3\output.json')

data = json.load(f)

print("Hello from langchain")

data_sign = [data["headline"], data["summary"], data["experiences"]]

print(data_sign)

summary_template = """
Given the information here: {information}, I want you to create:
1. A short summary
2. Two interesting facts about these
"""

summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)

llm = ChatOpenAI(temperature= 0, model_name="gpt-3.5-turbo", openai_api_key="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")

chain = LLMChain(llm=llm, prompt=summary_prompt_template)

print(chain.run(information = data_sign))