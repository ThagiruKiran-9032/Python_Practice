# Count function calls with a global variable
count = 0
def call_search():
    global count
    count += 1
    return count
print(call_search())
print(call_search())


# Count even numbers with a local variable
def count_even_numbers(numbers):
    even_count = 0
    for value in numbers:
        if value % 2 == 0:
            even_count += 1
    return even_count
print(count_even_numbers([2, 5, 8, 10]))


# Create a counter with an enclosing variable
def outer_counter():
    total = 0
    def inner_add(value):
        nonlocal total
        total += value
        return total
    return inner_add
counter = outer_counter()
print(counter(5))
print(counter(5))


# Count values with a closure
def make_counter():
    data = {}
    def add(value):
        data[value] = data.get(value, 0) + 1
        return data
    return add
counter = make_counter()
print(counter("A"))
print(counter("B"))
print(counter("A"))


#Search using a global limit
CONFIG = {"limit": 5}
def search_with_limit(values, target):
    global CONFIG
    for index, value in enumerate(values):
        if value == target and index < CONFIG["limit"]:
            return index
    return -1
print(search_with_limit([1, 4, 7, 9], 7))
CONFIG["limit"] = 3
print(search_with_limit([1, 4, 7, 9], 7))

