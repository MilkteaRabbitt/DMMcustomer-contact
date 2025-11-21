
from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI

load_dotenv()

try:
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.5)
    print("Attempting to invoke LLM...")
    result = llm.invoke("Hello, are you there?")
    print("Success!")
    print(result.content)
except Exception as e:
    print("Failed!")
    print(e)
