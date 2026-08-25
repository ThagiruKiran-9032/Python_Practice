n = 1221
original_number = n
reversed_number = 0

while n > 0:
    digit = n % 10
    reversed_number = reversed_number * 10 + digit
    n //= 10

if original_number == reversed_number:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")
