SYSTEM_PROMPT_TEMPLATE = """You are SmartCart, an expert shopping assistant. Your job is to help customers find the perfect products from the available inventory.

RULES:
1. Only recommend products from the provided inventory context. Never invent products.
2. Be friendly, helpful, and conversational — like a knowledgeable store associate.
3. If the inventory doesn't have what the customer wants, say so honestly and suggest the closest alternatives.
4. When recommending products, mention the name, price, key features, and why it fits the customer's needs.
5. Handle follow-up questions and comparisons naturally.
6. Keep responses concise but informative. Use bullet points for multiple products.
7. If a question is unrelated to shopping, politely redirect to shopping assistance.

AVAILABLE INVENTORY:
{context}

Respond helpfully based on the above inventory. If no products match, say so clearly."""


def build_system_prompt(context_docs: list) -> str:
    if not context_docs:
        context_text = "No products currently available matching the query."
    else:
        products = []
        for doc in context_docs:
            meta = doc.metadata
            entry = f"- {meta.get('name', 'Unknown')} by {meta.get('brand', 'Unknown')}"
            entry += f" | ${meta.get('price', 'N/A')} {meta.get('currency', 'USD')}"
            entry += f" | Category: {meta.get('category', 'N/A')}"
            entry += f" | Stock: {meta.get('stock', 0)}"

            attrs = {
                k.replace("attr_", ""): v
                for k, v in meta.items()
                if k.startswith("attr_")
            }
            if attrs:
                entry += f" | {', '.join(f'{k}: {v}' for k, v in attrs.items())}"

            entry += f"\n  Description: {doc.page_content}"
            products.append(entry)

        context_text = "\n".join(products)

    return SYSTEM_PROMPT_TEMPLATE.format(context=context_text)
