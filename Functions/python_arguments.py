# Find the largest number
def find_largest(numbers):
    largest = numbers[0]
    for value in numbers[1:]:
        if value > largest:
            largest = value
    return largest
numbers = [12, 45, 7, 89, 32]
print(find_largest(numbers))


# Find the second largest number
def second_largest(numbers):
    largest = max(numbers[0], numbers[1])
    second = min(numbers[0], numbers[1])

    for value in numbers[2:]:
        if value > largest:
            second = largest
            largest = value
        elif value > second:
            second = value
    return second
numbers = [10, 25, 8, 18, 30]
print(second_largest(numbers))


# Count the frequency of a number
def count_frequency(values, target):
    count = 0
    for value in values:
        if value == target:
            count += 1
    return count
values = [4, 2, 4, 6, 4, 2]
print(count_frequency(values, 4))


# Reverse a list
def reverse_list(numbers):
    reversed_numbers = []
    for value in range(len(numbers) - 1, -1, -1):
        reversed_numbers.append(numbers[value])
    return reversed_numbers
numbers = [1, 2, 3, 4, 5]
print(reverse_list(numbers))


# Check for a palindrome
def is_palindrome(text):
    return text == text[::-1]
print(is_palindrome("level"))
print(is_palindrome("python"))