# factorial recursively
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
print(factorial(5))


# Fibonacci number
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(7))


# Sum digits 
def sum_of_digits(n):
    if n < 10:
        return n
    return n % 10 + sum_of_digits(n // 10)
print(sum_of_digits(456))


# Reverse a string 
def reverse_string(text):
    if len(text) <= 1:
        return text
    return text[-1] + reverse_string(text[:-1])
print(reverse_string("python"))


# Check a palindrome 
def is_palindrome(text):
    if len(text) <= 1:
        return True
    if text[0] != text[-1]:
        return False
    return is_palindrome(text[1:-1])
print(is_palindrome("racecar"))
print(is_palindrome("python"))

