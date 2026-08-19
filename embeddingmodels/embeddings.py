from dotenv import load_dotenv
load_dotenv()

from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(
    model = 'text-embedding-3-large',
    dimensions=64
)

text = [
    "hello krishna",
    "nice name"
]

# vector = embeddings.embed_query("You are going to learn Gen AI")
vector = embeddings.embed_documents(text)

print(vector)