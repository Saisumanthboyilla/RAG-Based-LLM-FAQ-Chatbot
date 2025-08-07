from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from pymongo import MongoClient
import chromadb
import torch

# Check if CUDA (GPU) is available, otherwise use CPU
device = "cuda" if torch.cuda.is_available() else "cpu"

print(f"Using device: {device}")  # Print the selected device

# Initialize Embedding Model
embedding_model = HuggingFaceBgeEmbeddings(model_name="BAAI/bge-large-en", model_kwargs={"device": device})

# Initialize ChromaDB Client

# initializes a chromadb persistent client for storing and retriving embeddings effectively
# if the given path is not present it will automatically creates a new one

# setting up with a path to store the collections 
chroma_client = chromadb.PersistentClient(path="./chroma_db")

# Creating  Collection to store the embeddings 
collection_chroma_db = chroma_client.get_or_create_collection(name="faq_collection123")


# MongoDB Connection
mongo_client = MongoClient("mongodb://localhost:27017/")
db = mongo_client["event_question"]     # collection
collection = db["faq_questions"]      # database

faq_data = collection.find({}, {"_id": 0, "question": 1, "answer": 1})

# Fetch Data from MongoDB
for i, entry in enumerate(faq_data):   # it returns both index andthe each record
    question = entry["question"]
    answer = entry["answer"]

    # Generate embedding for the current question
    embedding = embedding_model.embed_query(question)

    # Print data before inserting
    print(f"Inserting ID: {i}")
    print(f"Question: {question}")
    print(f"Answer: {answer}")
    # print(f"Embedding (first 5 values): {embedding[:5]}...")  # Optional: print first 5 values
    print("-" * 50)

    # Insert into ChromaDB collection
    collection_chroma_db.add(
        ids=[str(i)],  # Use string IDs
        embeddings=[embedding],
        metadatas=[{"question": question, "answer": answer}]
    )

print("Data has been successfully inserted into ChromaDB!")
