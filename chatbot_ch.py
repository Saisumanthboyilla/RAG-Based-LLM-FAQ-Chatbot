import torch
import time
import ollama
import chromadb
from langchain_community.embeddings import HuggingFaceBgeEmbeddings

# Detect device (GPU or CPU)
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

# Initialize Embedding Model
embedding_model = HuggingFaceBgeEmbeddings(
    model_name="BAAI/bge-large-en",
    model_kwargs={"device": device}
)

# Connect to ChromaDB
chroma_client = chromadb.PersistentClient(path="chroma_db")  # Ensure path is correct
chroma_collection = chroma_client.get_collection("faq_collection123")

# Function to search for similar FAQ
def search_faq(query, top_k=3):
    print("user query ",query)
    query_embedding = embedding_model.embed_query(query)
    print("query_embedding:",query_embedding)
    results = chroma_collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    print("retrived results from chromadb ",results)

    # Extract top matches
    faqs = []
    for i in range(len(results["ids"][0])):
        faqs.append({
            "question": results["metadatas"][0][i]["question"],
            "answer": results["metadatas"][0][i]["answer"],
            "score": results["distances"][0][i]
        })
    return faqs


# Function to generate response using Llama 3.2
def generate_response(query):
    faqs = search_faq(query)
    print("cleaned _faq questions ",faqs)

    if not faqs:
        return "Sorry, I couldn't find relevant information."

    # Prepare prompt with retrieved FAQs
    context = ""
    for faq in faqs:
        context += f"Q: {faq['question']}\nA: {faq['answer']}\n"
    print("context ",context)
    prompt = f"""You are a helpful chatbot answering user questions based on the following FAQs:\n\n{context}\n\nUser: {query}\nAnswer:"""

    # Generate response using Llama 3.2
    response = ollama.chat(model="llama3.2:1b", messages=[{"role": "user", "content": prompt}])
    print("response",response)
    return response["message"]["content"]

# Chatbot loop
def chatbot():
    print("🤖 Chatbot is ready! Type 'exit' to stop.")
    while True:
        query = input("You: ")
        if query.lower() == "exit":
            print("Goodbye! 👋")
            break
        start_time = time.time()
        response = generate_response(query)
        end_time = time.time()
        total_time = start_time - end_time
        print(f"\nTotal Time Taken: {total_time:.2f} seconds")
        print(f"Bot: {response}\n")

# Run chatbot
if __name__ == "__main__":
    chatbot()
