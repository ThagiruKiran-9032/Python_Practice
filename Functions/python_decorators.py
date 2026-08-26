import time
# Time a sorting function
def execution_timer(func):
    def wrapper(values):
        start = time.time()
        result = func(values)
        end = time.time()
        print(f"{func.__name__} took {end - start:.6f} seconds")
        return result
    return wrapper
@execution_timer
def sort_numbers(values):
    return sorted(values)
print(sort_numbers([7, 2, 9, 1]))


# Validate that a list is not empty
def validate_list(func):
    def wrapper(values):
        if not values:
            raise ValueError("List cannot be empty")
        return func(values)
    return wrapper
@validate_list
def find_max(values):
    return max(values)
print(find_max([4, 9, 1, 7]))


# Log a function call
def log_calls(func):
    def wrapper(*args):
        print("calling", func.__name__)
        result = func(*args)
        print(result)
        return result
    return wrapper
@log_calls
def linear_search(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1
linear_search([4, 7, 2, 9], 7)


# Restrict the size of a list
def restrict_size(limit):
    def decorator(func):
        def wrapper(values):
            if len(values) > limit:
                raise ValueError(f"List size must be <= {limit}")
            return func(values)
        return wrapper
    return decorator
@restrict_size(5)
def sum_first_n(values):
    return sum(values)
print(sum_first_n([1, 2, 3, 4, 5]))


# Display frequency-count details
def debug_frequency(func):
    def wrapper(values):
        print(f"Input list: {values}")
        result = func(values)
        print(f"Result: {result}")
        return result
    return wrapper
@debug_frequency
def frequency_count(values):
    counts = {}
    for value in values:
        counts[value] = counts.get(value, 0) + 1
    return counts
print(frequency_count([3, 5, 3, 9, 5, 3]))

