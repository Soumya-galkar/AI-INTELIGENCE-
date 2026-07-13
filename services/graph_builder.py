# from utils.superbase_client import supabase


# def create_node(node_type, node_name):

#     existing = (
#         supabase
#         .table("graph_nodes")
#         .select("*")
#         .eq("node_type", node_type)
#         .eq("node_name", node_name)
#         .execute()
#     )

#     if existing.data:
#         return existing.data[0]["id"]

#     response = (
#         supabase
#         .table("graph_nodes")
#         .insert({
#             "node_type": node_type,
#             "node_name": node_name
#         })
#         .execute()
#     )

#     return response.data[0]["id"]


def create_edge(source, target, relationship):

    supabase.table("graph_edges").insert({

        "source_node": source,

        "target_node": target,

        "relationship": relationship

    }).execute()

from utils.superbase_client import supabase


def get_or_create_node(node_type, node_name, metadata=None):

    if metadata is None:
        metadata = {}

    existing = (
        supabase
        .table("graph_nodes")
        .select("*")
        .eq("node_type", node_type)
        .eq("node_name", node_name)
        .execute()
    )

    if existing.data:
        return existing.data[0]["id"]

    response = (
        supabase
        .table("graph_nodes")
        .insert({
            "node_type": node_type,
            "node_name": node_name,
            "metadata": metadata
        })
        .execute()
    )

    return response.data[0]["id"]

def create_edge(source,target,relation):
    existing = ( 
        supabase
        .table("graph_edges")
        .select("*")
        .eq("source_node",source)
        .eq("target_node",target)
        .eq("relationship",relation)
        .execute()
    )

    if existing.data:
        return 
    
    supabase.table("graph_edges").insert({
        "source_node":source,
        "target_node":target,
        "relationship":relation
    }).execute()

