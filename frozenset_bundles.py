"""
1️⃣ Research frozenset

What is frozenset:
A frozenset is an immutable, hashable version of a Python set. Once created, its elements cannot be added, removed, or modified.

Difference between set vs frozenset:
- Mutability: A `set` is mutable (you can use .add(), .remove()), while a `frozenset` is immutable.
- Hashability: A `set` is unhashable and cannot be used as a dictionary key or an element of another set. A `frozenset` is hashable and can be used as a key in a dictionary or stored inside another set.

When you would use it in real systems:
- Caching/Memoization: As a cache key when order doesn't matter (e.g., caching results for a given set of tags or categories).
- Advanced Data Structures: Using them as keys in dictionaries for composite keys like bundle discounts.
- Data Integrity: When you want to pass a set of configuration options or allowed states and guarantee they won't be modified.
"""

import timeit

# 2️⃣ Bundle Discount System
bundle_discounts = {
    frozenset({'Electronics', 'Books'}): 10,
    frozenset({'Electronics', 'Home'}): 5,
    frozenset({'Books', 'Home', 'Electronics'}): 15,
    frozenset({'Clothing', 'Home'}): 8
}

# 3️⃣ Bundle Checker Function
def check_bundle_discount(cart_categories):
    """
    Checks if a cart (represented as a set or iterable of categories) matches any bundle deals.
    Returns the maximum applicable discount.
    """
    cart_set = frozenset(cart_categories)
    max_discount = 0
    for bundle, discount in bundle_discounts.items():
        if bundle.issubset(cart_set):
            if discount > max_discount:
                max_discount = discount
    return max_discount

# 4️⃣ Performance Benchmark
if __name__ == "__main__":
    # Test Bundle Checker
    test_cart = {'Electronics', 'Books', 'Clothing'}
    print(f"Cart Categories: {test_cart}")
    print(f"Applicable Discount: {check_bundle_discount(test_cart)}%")

    # Benchmark set vs frozenset
    print("\nRunning benchmark (100000 iterations)...")
    set_time = timeit.timeit("s = {'Electronics', 'Books', 'Clothing'}", number=100000)
    frozenset_time = timeit.timeit("fs = frozenset({'Electronics', 'Books', 'Clothing'})", number=100000)

    print(f"Set creation time:       {set_time:.6f} seconds")
    print(f"Frozenset creation time: {frozenset_time:.6f} seconds")

    # Benchmark Results (100000 iterations):
    # Set creation time:       ~0.0039 seconds
    # Frozenset creation time: ~0.0080 seconds
    # Conclusion: `set` creation is typically slightly faster because `frozenset` 
    # has extra overhead for immutability during creation, though lookup speeds are comparable.
