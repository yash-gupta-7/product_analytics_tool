from collections import namedtuple

# 1️⃣ Define a Named Tuple
Product = namedtuple("Product", ["id", "name", "category", "price"])

# 2️⃣ Create a Product Catalog
catalog = [
    Product(1, "Laptop", "Electronics", 75000),
    Product(2, "Phone", "Electronics", 40000),
    Product(3, "Headphones", "Electronics", 5000),
    Product(4, "Monitor", "Electronics", 15000),
    Product(5, "T-Shirt", "Clothing", 500),
    Product(6, "Jeans", "Clothing", 1500),
    Product(7, "Jacket", "Clothing", 3000),
    Product(8, "Sneakers", "Clothing", 2500),
    Product(9, "Clean Code", "Books", 800),
    Product(10, "Python Crash Course", "Books", 900),
    Product(11, "Design Patterns", "Books", 1200),
    Product(12, "Deep Work", "Books", 500),
    Product(13, "Desk Lamp", "Home", 1200),
    Product(14, "Office Chair", "Home", 5000),
    Product(15, "Coffee Mug", "Home", 300)
]

# 3️⃣ Customer Cart Sets
customer_1_cart = {catalog[0], catalog[1], catalog[8], catalog[12], catalog[14]}
customer_2_cart = {catalog[0], catalog[2], catalog[8], catalog[13]}
customer_3_cart = {catalog[0], catalog[1], catalog[4], catalog[5], catalog[6]}
customer_4_cart = {catalog[0], catalog[9], catalog[10], catalog[14]}
customer_5_cart = {catalog[0], catalog[1], catalog[2], catalog[7]}

all_carts = [customer_1_cart, customer_2_cart, customer_3_cart, customer_4_cart, customer_5_cart]

# 4️⃣ Analyze Shopping Behaviour
# (a) Bestsellers (Products appearing in ALL carts)
bestsellers = set.intersection(*all_carts)

# (b) Catalog Reach (Products appearing in ANY cart)
catalog_reach = set.union(*all_carts)

# (c) Exclusive Purchases (Products only customer_1 bought)
other_carts_union = set.union(*all_carts[1:])
exclusive_purchases = customer_1_cart.difference(other_carts_union)

# 5️⃣ Product Recommendation
def recommend_products(customer_cart, all_carts):
    """Suggest products other customers bought but this customer didn't."""
    other_carts = [cart for cart in all_carts if cart != customer_cart]
    if not other_carts:
        return set()
    other_purchases = set.union(*other_carts)
    return other_purchases - customer_cart

# 6️⃣ Category Summary
def category_summary():
    """Return dictionary grouping product names by category."""
    categories = {"Electronics", "Clothing", "Books", "Home"}
    summary = {
        category: {product.name for product in catalog if product.category == category}
        for category in categories
    }
    return summary

if __name__ == "__main__":
    print("--- Shopping Behaviour Analysis ---")
    print("\n1. Bestsellers (In all carts):")
    for p in bestsellers:
        print(f" - {p.name}")

    print("\n2. Catalog Reach (In any cart):")
    for p in catalog_reach:
        print(f" - {p.name}")

    print("\n3. Exclusive Purchases (Customer 1 only):")
    for p in exclusive_purchases:
        print(f" - {p.name}")

    print("\n4. Product Recommendations (for Customer 1):")
    recs = recommend_products(customer_1_cart, all_carts)
    for p in recs:
        print(f" - {p.name}")

    print("\n5. Category Summary:")
    summary = category_summary()
    for cat, prods in summary.items():
        print(f" {cat}: {prods}")
