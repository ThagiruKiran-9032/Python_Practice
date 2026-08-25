first = 2
second = 2
third = 1
fourth = 1
fifth = 2
candidate = 2
occurrences = 0

if first == candidate:
    occurrences += 1
if second == candidate:
    occurrences += 1
if third == candidate:
    occurrences += 1
if fourth == candidate:
    occurrences += 1
if fifth == candidate:
    occurrences += 1

if occurrences > 5 // 2:
    print("Majority element:", candidate)
else:
    print("No majority element exists")