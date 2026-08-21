num = [5, 1, 4, 2, 8]

for i in range(len(num) - 1):
    swapped = False

    for j in range(len(num) - 1 - i):
        if num[j] > num[j + 1]:
            num[j], num[j + 1] = num[j + 1], num[j]
            swapped = True

    if not swapped:
        break

print("Sorted list:", num)
