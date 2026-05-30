import logging
from app.dependencies import get_inventory_service
from app.core.inventory.models import Product

logger = logging.getLogger("smartcart")

DEMO_TENANT_ID = "demo"

DEMO_PRODUCTS = [
    Product(
        id="shirt-001",
        name="Ocean Breeze Linen Shirt",
        description="Lightweight linen shirt perfect for beach outings and summer travel. Relaxed fit with breathable fabric.",
        category="shirts",
        price=49.99,
        brand="CoastalWear",
        image_url="/images/products/shirt-001.jpg",
        stock=25,
        attributes={"color": "sky blue", "material": "linen", "fit": "relaxed", "occasion": "casual"},
    ),
    Product(
        id="shirt-002",
        name="Crimson Classic Oxford",
        description="Timeless oxford shirt in deep red. Versatile enough for office or weekend brunches.",
        category="shirts",
        price=59.99,
        brand="UrbanThread",
        image_url="/images/products/shirt-002.jpg",
        stock=18,
        attributes={"color": "red", "material": "cotton", "fit": "regular", "occasion": "smart casual"},
    ),
    Product(
        id="shirt-003",
        name="Midnight Navy Polo",
        description="Premium piqué polo in navy blue. Ribbed collar and moisture-wicking fabric for active days.",
        category="shirts",
        price=39.99,
        brand="ActiveEdge",
        image_url="/images/products/shirt-003.jpg",
        stock=30,
        attributes={"color": "navy blue", "material": "piqué cotton", "fit": "slim", "occasion": "casual"},
    ),
    Product(
        id="shirt-004",
        name="Tropical Print Camp Shirt",
        description="Bold tropical print camp collar shirt. Stand out at parties and beach gatherings.",
        category="shirts",
        price=44.99,
        brand="CoastalWear",
        image_url="/images/products/shirt-004.jpg",
        stock=15,
        attributes={"color": "multicolor", "material": "viscose", "fit": "relaxed", "occasion": "party"},
    ),
    Product(
        id="pants-001",
        name="Urban Slim Chinos",
        description="Modern slim-fit chinos with stretch. Comfortable all-day wear from desk to dinner.",
        category="pants",
        price=64.99,
        brand="UrbanThread",
        image_url="/images/products/pants-001.jpg",
        stock=22,
        attributes={"color": "khaki", "material": "stretch cotton", "fit": "slim", "occasion": "smart casual"},
    ),
    Product(
        id="pants-002",
        name="Relaxed Cargo Joggers",
        description="Utility-inspired cargo joggers with elastic waist. Multiple pockets for everyday carry.",
        category="pants",
        price=54.99,
        brand="ActiveEdge",
        image_url="/images/products/pants-002.jpg",
        stock=20,
        attributes={"color": "olive green", "material": "cotton twill", "fit": "relaxed", "occasion": "casual"},
    ),
    Product(
        id="jacket-001",
        name="Storm Shield Windbreaker",
        description="Lightweight windbreaker with water-resistant coating. Packable design for travel.",
        category="jackets",
        price=89.99,
        brand="ActiveEdge",
        image_url="/images/products/jacket-001.jpg",
        stock=12,
        attributes={"color": "black", "material": "nylon", "fit": "regular", "occasion": "outdoor"},
    ),
    Product(
        id="jacket-002",
        name="Heritage Denim Jacket",
        description="Classic denim jacket with vintage wash. A wardrobe essential for layering.",
        category="jackets",
        price=79.99,
        brand="UrbanThread",
        image_url="/images/products/jacket-002.jpg",
        stock=14,
        attributes={"color": "medium wash", "material": "denim", "fit": "regular", "occasion": "casual"},
    ),
    Product(
        id="shoes-001",
        name="TrailBlazer Running Shoes",
        description="High-performance running shoes with responsive cushioning and breathable mesh upper. Ideal for marathons and long-distance running.",
        category="shoes",
        price=129.99,
        brand="ActiveEdge",
        image_url="/images/products/shoes-001.jpg",
        stock=20,
        attributes={"color": "white/blue", "material": "mesh/rubber", "fit": "true to size", "occasion": "sports"},
    ),
    Product(
        id="shoes-002",
        name="Leather Chelsea Boots",
        description="Premium leather Chelsea boots with elastic side panels. Sophisticated style for any occasion.",
        category="shoes",
        price=149.99,
        brand="UrbanThread",
        image_url="/images/products/shoes-002.jpg",
        stock=10,
        attributes={"color": "brown", "material": "genuine leather", "fit": "true to size", "occasion": "formal"},
    ),
    Product(
        id="shoes-003",
        name="Canvas Slip-On Sneakers",
        description="Easy-going canvas sneakers with cushioned insole. Effortless style for everyday wear.",
        category="shoes",
        price=34.99,
        brand="CoastalWear",
        image_url="/images/products/shoes-003.jpg",
        stock=35,
        attributes={"color": "white", "material": "canvas", "fit": "true to size", "occasion": "casual"},
    ),
    Product(
        id="acc-001",
        name="Aviator Sunglasses",
        description="Classic aviator sunglasses with UV400 protection and polarized lenses.",
        category="accessories",
        price=29.99,
        brand="CoastalWear",
        image_url="/images/products/acc-001.jpg",
        stock=40,
        attributes={"color": "gold/green", "material": "metal frame", "occasion": "outdoor"},
    ),
    Product(
        id="acc-002",
        name="Minimalist Leather Belt",
        description="Sleek leather belt with brushed metal buckle. Essential finishing touch for any outfit.",
        category="accessories",
        price=24.99,
        brand="UrbanThread",
        image_url="/images/products/acc-002.jpg",
        stock=30,
        attributes={"color": "black", "material": "leather", "occasion": "formal"},
    ),
    Product(
        id="shirt-005",
        name="Sunset Stripe Beach Shirt",
        description="Relaxed beach shirt with gradient sunset stripes. Perfect for coastal vibes and vacation looks.",
        category="shirts",
        price=42.99,
        brand="CoastalWear",
        image_url="/images/products/shirt-005.jpg",
        stock=20,
        attributes={"color": "orange/blue", "material": "cotton blend", "fit": "relaxed", "occasion": "beach"},
    ),
    Product(
        id="pants-003",
        name="Performance Track Pants",
        description="Athletic track pants with moisture-wicking fabric and zippered pockets. From gym to street.",
        category="pants",
        price=49.99,
        brand="ActiveEdge",
        image_url="/images/products/pants-003.jpg",
        stock=25,
        attributes={"color": "black", "material": "polyester", "fit": "tapered", "occasion": "sports"},
    ),
]


def seed_demo_inventory():
    """Seed demo tenant inventory on startup if not already populated."""
    service = get_inventory_service()
    existing_count = service.get_product_count(DEMO_TENANT_ID)

    if existing_count >= len(DEMO_PRODUCTS):
        logger.info(f"Demo inventory already has {existing_count} products. Skipping seed.")
        return

    count = service.sync_products(DEMO_TENANT_ID, DEMO_PRODUCTS)
    logger.info(f"Seeded {count} demo products.")
