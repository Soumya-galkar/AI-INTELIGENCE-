from sentence_transformers import SentenceTransformer
from utils.superbase_client import supabase

# Load once when FastAPI starts
model = SentenceTransformer("all-MiniLM-L6-v2")


def create_query_embedding(question: str):
    embedding = model.encode(question)
    return embedding.tolist()


def search_chunks(query_embedding, match_count=5):

    response = supabase.rpc(
        "match_document_chunks",
        {
            "query_embedding": query_embedding,
            "match_count": match_count
        }
    ).execute()

    return response.data