import os
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_ollama import ChatOllama


# importing env variable
load_dotenv(True)

# making prompt template 
numerology_template = PromptTemplate(
    input = ["date_of_birth"],
    template = "You are a numerology expert based on {date_of_birth} you tell people about" \
    "1. life in general " \
    "2. About personality " \
    "3. What they need to do to improve"
)


# making prompt 
prompt = numerology_template.format(date_of_birth= "04 Aug 1991")


# Making instance of LLM
ollama = ChatOllama(model="gpt-oss")

# making llm call 
ollama_response = ollama.invoke(prompt).content

# printint result 
print(ollama_response)
