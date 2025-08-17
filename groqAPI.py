from groq import Groq
from embeddings import query_pinecone

client = Groq(api_key='YOUR_API_KEY')

def groq_assistance(user_query):
    products=query_pinecone(user_query,5)

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful shopping assistant. Given a list of products, respond to queries of consumer."
            },
            {
                "role": "user",
                "content": f"List of products:\n{products}\nConsumer Query:\n{user_query}"
            }
        ],
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
        stream=False,
        stop=None,
    )

    # return completion.choices[0].message.content
    print(completion.choices[0].message.content)

groq_assistance("Find best laptops under 50000")
