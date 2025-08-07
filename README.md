# RAG-Based-LLM-FAQ-Chatbot
A smart FAQ chatbot using LLMs and RAG. Q&amp;A data is read from a JSON file (converted from PDF), embeddings are generated using Hugging Face's BGE model, and stored in ChromaDB. On query, relevant answers are retrieved via similarity search and refined with an LLM for accurate, human-like responses.
# 🤖 FAQ Chatbot using RAG (Retrieval-Augmented Generation)

Welcome to my RAG-based FAQ chatbot project! This chatbot can answer your questions by understanding and referring to a list of FAQs. It uses powerful AI and search techniques to find the best answers.

---

## 🧠 What is RAG? (Easy Explanation)

**RAG** stands for **Retrieval-Augmented Generation**.

Let’s say you ask a question like:  
➡️ “How can I reset my password?”

A regular AI model might try to guess the answer. But RAG does something smarter:
1. 🗃️ It **searches** your documents (like FAQs) for similar questions.
2. 🧠 Then, it uses a smart language model (LLM) to **generate** a good answer using the info it just found.

✅ It doesn’t guess — it reads and replies.

---

## 🚀 What This Project Does

This project creates a **local chatbot** that:
- Reads FAQ data stored in MongoDB
- Converts the questions into **embeddings** using a model
- Stores those embeddings in **ChromaDB**
- Lets you ask any question
- Uses **RAG** to search related FAQs
- Responds using **LLaMA 3.2B** (running locally with **Ollama**)

---

## 📂 Project Structure

```
📦 RAG-Chatbot
├── data_to_chroma.py        # Loads FAQ data from MongoDB into ChromaDB
├── chatbot_ch.py            # Runs the chatbot (RAG system)
├── chroma_db/               # Folder auto-created to store vector database
├── requirements.txt         # Dependencies (create this file)
├── .env (optional)          # For storing secrets (not in repo)
└── README.md                # Project documentation (this file)
```

---

## 🛠️ Technologies Used

| Component        | Tool                             |
|------------------|----------------------------------|
| Embedding Model  | `BAAI/bge-large-en`              |
| Vector DB        | `ChromaDB`                       |
| LLM              | `LLaMA 3.2B` via Ollama          |
| Data Source      | `MongoDB`                        |
| Framework        | `LangChain Embeddings`           |
| Language         | `Python`                         |

---

## ✅ Features

- Answers questions using your own FAQs
- Works completely **offline and locally**
- Fast and accurate using **vector search**
- Modular and easy to customize

---

## ⚙️ How to Set Up & Run

### 1. Clone the Repository
```bash
git clone https://github.com/Saisumanthboyilla/rag-chatbot.git
cd rag-chatbot
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

> You need Python 3.8+ and Ollama installed for LLaMA.

### 3. Start MongoDB
Make sure MongoDB is running locally:
```bash
mongod
```

Insert your FAQ documents into MongoDB:
- **Database**: `event_question`
- **Collection**: `faq_questions`
- Example document format:
```json
{
  "question": "How do I contact customer service?",
  "answer": "You can contact us at support@example.com"
}
```

### 4. Run the Data Loader
This converts FAQ questions into embeddings and stores them in ChromaDB.
```bash
python data_to_chroma.py
```

### 5. Start the Chatbot
Now you can ask your questions to the bot!
```bash
python chatbot_ch.py
```

Type your question and press Enter.  
To exit, type `exit`.

---

## 💬 Example

```
You: How can I return my product?
Bot: You can return your product within 30 days of delivery with the original receipt.
```

---

## 📌 To-Do

- [ ] Add a simple Streamlit or Gradio UI
- [ ] Include sample MongoDB import script
- [ ] Add Dockerfile for easy containerization

---

## 📷 Screenshot (optional)

*(Insert a screenshot of your chatbot if you want)*

  

## 👤 Author

**Boyilla Sai Sumanth**  
Aspiring Data Scientist | Machine Learning & Generative AI Enthusiast  
🔗 [LinkedIn](https://www.linkedin.com/in/sai-sumanth-boyilla/)

---
