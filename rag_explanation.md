# 📄 Retrieval-Augmented Generation (RAG)

## 🔹 What is RAG?
RAG is a technique that improves LLM responses by adding external knowledge.

---

## 🔹 Steps:
1. Load documents (PDF/text)
2. Split into small chunks
3. Convert chunks into embeddings
4. Store in vector database (FAISS)
5. Retrieve relevant chunks based on question
6. Pass context to LLM
7. Generate final answer

---

## 🔹 Why RAG is Important
- Reduces hallucinations
- Improves accuracy
- Uses private/custom data
