# Python Tuples and Sets: Interview Insights

## Q1 Conceptual: The Tuple Immutability Trap

**Consider:**
```python
t = ([1,2], [3,4])
t[0][0] = 99
```

### Explantion:
**It works.** Running `t[0][0] = 99` will successfully change the first element of the first list to `99`, resulting in `t` being `([99, 2], [3, 4])`.

### Why it works:
- **Tuple Immutability:** A tuple is immutable in the sense that the **references** it holds cannot be changed. Once `t` is created, it will always point to those two specific list objects.
- **List Mutability:** The objects contained *inside* the tuple (the lists) are mutable. While you cannot swap the list for a different object (e.g., `t[0] = [10, 20]` would fail), you can modify the contents of the list that the tuple is pointing to.

### What this reveals:
This reveals that Python's immutability is **shallow**. A tuple ensures that its member references are constant, but it does not recursively enforce immutability on the objects those references point to.

---

## Q2 Coding: Duplicate Detection (O(n))

To find duplicates in $O(n)$ using only set operations, we can compare the length of the list with a set, or more accurately, use two sets to track seen items and duplicate items.

```python
def find_duplicates(lst):
    seen = set()
    dupes = set()
    for x in lst:
        if x in seen:
            dupes.add(x)
        else:
            seen.add(x)
    return dupes
```

**Complexity:** $O(n)$ time because set lookups and additions are $O(1)$ on average.

---

## Q3 Debug Problem: Symmetric Difference

### Why the bug happens:
The current code `set(a) - set(b)` performs a **set difference**. It identifies elements that are in `a` but NOT in `b`. 
In the test case `[1,2,3]` and `[3,4,5]`:
- `set(a)` is `{1, 2, 3}`
- `set(b)` is `{3, 4, 5}`
- `{1, 2, 3} - {3, 4, 5}` yields `{1, 2}`, which ignores the unique elements in `b` (`4` and `5`).

### The Fix:
We need the **symmetric difference**, which contains elements that are in either set, but not in both. This can be done using the `^` operator or the `.symmetric_difference()` method.

**Fixed Function:**
```python
def unique_to_each(a, b):
    # Symmetric difference: (A - B) | (B - A)
    result = set(a) ^ set(b) 
    return list(result)
```

**Test Result:**
`unique_to_each([1,2,3], [3,4,5])` -> `{1, 2, 4, 5}` (Expected)
