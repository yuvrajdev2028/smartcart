from pinecone import Pinecone
import time
import json

pc = Pinecone(api_key="PINECONE_API_KEY")

index_name = "smartcart"

if not pc.has_index(index_name):
    pc.create_index_for_model(
        name=index_name,
        cloud="aws",
        region="us-east-1",
        embed={
            "model":"llama-text-embed-v2",
            "field_map":{"text": "title"}
        }
    )

dense_index = pc.Index(index_name)

with open('inventory.json', 'r') as f:
    data = json.load(f)

dense_index.upsert_records("inventory", data)

def query_pinecone(query,top_k):
    results = dense_index.search(
        namespace="inventory",
        query={
            "top_k": top_k,
            "inputs": {
                'text': query,
            }
        }
    )

    products=""
    for hit in results['result']['hits']:
        products=products+f"category: {hit['fields']['category']:<10} \n text: {hit['fields']['title']:<50}\n"
    
    return products
