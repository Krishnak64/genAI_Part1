from dotenv import load_dotenv

load_dotenv()

from langchain_mistralai import ChatMistralAI

model = ChatMistralAI(model = "mistral-small-2603", temperature=0.9, max_tokens=20)

response = model.invoke("write a poem on AI?")

print(response.content)