# from services.search import create_query_embedding, search_chunks
# from services.gemini_service import ask_gemini

# def build_prompt(question, chunks):

#     context = ""

#     sources = []

#     for chunk in chunks:
#         context += f"""
# Page: {chunk['page_number']}
# Content:
# {chunk['chunk_text']}

# """

#         sources.append(
#             {
#                 "document_id": chunk["document_id"],
#     "page": chunk["page_number"],
#     "chunk": chunk["chunk_number"],
#     "similarity": round(chunk["similarity"], 3)
#             }
#         )

#     prompt = f"""
# You are an AI Industrial Knowledge Assistant.

# Answer ONLY using the context provided below.

# If the answer is not available in the context,
# reply:

# "I couldn't find this information in the uploaded documents."

# -------------------------
# CONTEXT

# {context}

# -------------------------

# QUESTION

# {question}

# -------------------------

# Give a clear and concise answer.
# """

#     return prompt, sources


# def rag_answer(question):

#     embedding = create_query_embedding(question)

#     chunks = search_chunks(embedding)

#     prompt, sources = build_prompt(question, chunks)

#     answer = ask_gemini(prompt)

#     confidence = 0  # Placeholder for confidence score, can be improved with actual model output
#     if chunks:
#         confidence = round(chunks[0]["similarity"] * 100, 2)
#     return {
#     "answer": answer,
#     "confidence": confidence,
#     "sources": sources
# }

# from services.search import search_documents
# from services.gemini_service import ask_gemini


# def rag_answer(question):

#     results = search_documents(question)

#     context = ""

#     for chunk in results:
#         context += chunk["chunk_text"]
#         context += "\n\n"

#     answer = ask_gemini(question, context)

#     return {
#         "answer": answer,
#         "sources": results
#     }


# new
from services.search import create_query_embedding, search_chunks
from services.gemini_service import ask_gemini


def rag_answer(question: str):

    # Generate embedding
    query_embedding = create_query_embedding(question)

    # Search similar chunks
    chunks = search_chunks(query_embedding)

    if not chunks:
        return {
            "answer": "No relevant documents found.",
            "sources": [],
            "confidence": 0
        }

    context = ""

    sources = []

    for chunk in chunks:

        context += f"""
Document ID: {chunk['document_id']}
Page: {chunk['page_number']}

{chunk['chunk_text']}

-------------------------------------
"""

        sources.append({
            "document_id": chunk["document_id"],
            "page_number": chunk["page_number"],
            "similarity": round(chunk["similarity"], 3)
        })

    answer = ask_gemini(question, context)

    confidence = round(chunks[0]["similarity"] * 100, 2)

    return {
        "question": question,
        "answer": answer,
        "confidence": confidence,
        "sources": sources
    }