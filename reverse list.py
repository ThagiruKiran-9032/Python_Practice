num = [1, 2, 3, 4, 5]
reversed_numbers = []

for i in range(len(num) - 1, -1, -1):
    reversed_numbers.append(num[i])

print("Original list:", num)
print("Reversed list:", reversed_numbers)
