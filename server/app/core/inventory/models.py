from pydantic import BaseModel


class Product(BaseModel):
    id: str
    name: str
    description: str
    category: str
    price: float
    currency: str = "USD"
    brand: str
    image_url: str | None = None
    stock: int = 0
    attributes: dict = {}

    def to_document_text(self) -> str:
        """Flat text for embedding."""
        attrs = ", ".join(f"{k}: {v}" for k, v in self.attributes.items())
        parts = [
            f"{self.name} by {self.brand}",
            self.description,
            f"Category: {self.category}",
            f"Price: {self.currency} {self.price}",
        ]
        if attrs:
            parts.append(attrs)
        return ". ".join(parts)

    def to_metadata(self) -> dict:
        """Structured metadata stored alongside the vector."""
        meta = {
            "product_id": self.id,
            "name": self.name,
            "category": self.category,
            "price": self.price,
            "currency": self.currency,
            "brand": self.brand,
            "stock": self.stock,
        }
        if self.image_url:
            meta["image_url"] = self.image_url
        for k, v in self.attributes.items():
            if isinstance(v, (str, int, float, bool)):
                meta[f"attr_{k}"] = v
        return meta
