from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

information = '''
In this quickstart we'll show you how to:

Get setup with LangChain, LangSmith and LangServe
Use the most basic and common components of LangChain: prompt templates, models, and output parsers
Use LangChain Expression Language, the protocol that LangChain is built on and which facilitates component chaining
Build a simple application with LangChain
Trace your application with LangSmith
Serve your application with LangServe
That's a fair amount to cover! Let's dive in.
'''

print("Hello from langchain")

summary_template = """
Given the information here: {information}, I want you to create:
1. A short summary
2. Two interesting facts about these
"""

summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)

llm = ChatOpenAI(temperature= 0, model_name="gpt-3.5-turbo", openai_api_key="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")

chain = LLMChain(llm=llm, prompt=summary_prompt_template)

print(chain.run(information))