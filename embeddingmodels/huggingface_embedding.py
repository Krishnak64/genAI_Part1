from dotenv import load_dotenv
load_dotenv()

from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name = "sentence-transformers/al-MiniM-L6-v2" # model size is very large
)

text = [
    "hello krishna",
    "nice name"
]

# vector = embeddings.embed_query("You are going to learn Gen AI")
vector = embeddings.embed_documents(text)
