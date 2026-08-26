# maximum of any number of values
def find_max(*numbers):
    maximum = numbers[0]
    for value in numbers[1:]:
        if value > maximum:
            maximum = value
    return maximum
print(find_max(3, 7, 9, 1, 5))


# Sum any number of values
def sum_numbers(*numbers):
    total = 0
    for value in numbers:
        total += value
    return total
print(sum_numbers(2, 3, 4, 5))


# Find the average of values
def average_numbers(*numbers):
    return sum(numbers) / len(numbers)
print(average_numbers(10, 20, 30, 40))


# Keep the even values
def keep_even(*numbers):
    result = []
    for value in numbers:
        if value % 2 == 0:
            result.append(value)
    return result
print(keep_even(1, 2, 3, 4, 5, 6))


# Sort any number of values
def sort_values(*numbers):
    return sorted(numbers)
print(sort_values(9, 3, 7, 1))

