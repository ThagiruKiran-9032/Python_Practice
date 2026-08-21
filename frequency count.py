numbers = [2, 4, 2, 7, 4, 2, 9]
frequency = {}

for number in numbers:
    if number in frequency:
        frequency[number] += 1
    else:
        frequency[number] = 1

print("Number frequencies:", frequency)
