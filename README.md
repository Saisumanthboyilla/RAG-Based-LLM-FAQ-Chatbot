# RAG-Based-LLM-FAQ-Chatbot
A smart FAQ chatbot using LLMs and RAG. Q&amp;A data is read from a JSON file (converted from PDF), embeddings are generated using Hugging Face's BGE model, and stored in ChromaDB. On query, relevant answers are retrieved via similarity search and refined with an LLM for accurate, human-like responses.
