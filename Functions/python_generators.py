# Generate even numbers
def even_numbers(start, end):
    current = start
    while current <= end:
        if current % 2 == 0:
            yield current
        current += 1
print(list(even_numbers(2, 10)))


# Generate square numbers
def square_numbers(n):
    for value in range(1, n + 1):
        yield value * value
print(list(square_numbers(5)))


# Generate Fibonacci numbers
def fibonacci_generator(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b
print(list(fibonacci_generator(20)))


# Generate a custom range
def custom_range(start, stop, step=1):
    current = start
    while current < stop:
        yield current
        current += step
print(list(custom_range(1, 10, 2)))


# Generate odd numbers
def filter_odds(values):
    for value in values:
        if value % 2 != 0:
            yield value
print(list(filter_odds([1, 2, 3, 4, 5, 6])))

