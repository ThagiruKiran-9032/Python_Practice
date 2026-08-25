num = [34, 12, 89, 45, 67]
largest = num[0]

for i in num[1:]:
    if i > largest:
        largest = i

print("Largest number:", largest)
