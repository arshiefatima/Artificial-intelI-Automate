

from typing import List

documents = [
    "AI Agents can take actions using tools.",
    "RAG improves LLM answers using external knowledge.",
    "LangChain helps build LLM applications easily."
]

def retrieve(query: str, docs: List[str]) -> List[str]:
    """
    Simple retrieval simulation (keyword match)
    """
    return [doc for doc in docs if query.lower() in doc.lower() or any(word in doc for word in query.split())]

def generate_answer(query: str):
    context = retrieve(query, documents)

    prompt = f"""
    Question: {query}
    Context: {context}
    Answer based on context:
    """


    return "This is a simulated LLM response using retrieved context."


query = "What is RAG?"
print(generate_answer(query))
