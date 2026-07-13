from utils.superbase_client import supabase


def save_document_metadata(document_id, metadata):

   response = supabase.table("document_metadata").insert({

        "document_id": document_id,

        "document_type": metadata["document_type"],

        "department": metadata["department"],

        "summary": metadata["summary"],

        "maintenance_type": metadata["maintenance_type"],

        "risk_level": metadata["risk_level"],

        "equipment": metadata["equipment"],

        "keywords": metadata["keywords"]

    }).execute()
   
   return response