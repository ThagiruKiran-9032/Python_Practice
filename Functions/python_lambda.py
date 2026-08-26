# Square numbers with map and lambda
numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x: x * x, numbers))
print(result)


# Keep even numbers with filter and lambda
values = [1, 2, 3, 4, 5, 6]
result = list(filter(lambda x: x % 2 == 0, values))
print(result)


# Sort pairs by their number
items = [("A", 40), ("B", 12), ("C", 28)]
result = sorted(items, key=lambda item: item[1])
print(result)


# Sort students by marks
students = [
    {"name": "Ava", "marks": 88},
    {"name": "Ben", "marks": 92},
    {"name": "Cia", "marks": 88},
]
result = sorted(students, key=lambda s: s["marks"])
print(result)


# Transform words with map and lambda
words = ["cat", "elephant", "dog", "lion"]
result = list(map(lambda word: word.upper() if len(word) >= 3 else word, words))
print(result)

