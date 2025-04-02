from groq import Groq
import os

client = Groq(api_key=os.environ['GROQ_API_KEY'])

def groq_assistance(products,user_query):
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

    return completion.choices[0].message.content

def search_query_gen(prompt):
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": '''You are a helpful assistant. Given a consumer requirement, 
                                your task is to generate a search query for amazon containing a single product, 
                                brand name, specs about the product(if specified) and price limitations (if specified). 
                                Generate a single short query, not multiple queries. Don't put brand names in search query 
                                if not already specified in the consumer requirement. Only use categorical keywords and not ambiguous words.'''
            },
            {
                "role": "user",
                "content": f"Consumer requirement:\n{prompt}"
            },
        ],
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
        stream=False,
        stop=None,
    )

    return completion.choices[0].message.content

def prompt_categorisation(prompt):
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": '''You are a helpful assistant. Given a consumer prompt, your task is to classify it as either 'search request' 
                                or 'consumer query'. Output only one of these two categories and no other text. 'Consumer query' will always have indicators 
                                showing a list of results is already provided to consumer and he is querying on it. 'Search request' will have no such indicators.'''
            },
            {
                "role": "user",
                "content": f"Consumer Prompt:\n{prompt}"
            }
        ],
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
        stream=False,
        stop=None,
    )

    return completion.choices[0].message.content