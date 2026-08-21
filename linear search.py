numbers = [10, 25, 7, 42, 18]
target = 42

found = False
for index in range(len(numbers)):
    if numbers[index] == target:
        print("Found", target, "at index", index)
        found = True
        break

if not found:
    print(target, "was not found")
