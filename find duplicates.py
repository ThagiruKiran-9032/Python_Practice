numbers = [4, 2, 7, 4, 9, 2, 1]
seen = set()
duplicates = set()

for number in numbers:
    if number in seen:
        duplicates.add(number)
    else:
        seen.add(number)

print("Duplicate values:", list(duplicates))
