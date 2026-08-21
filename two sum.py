num = [2, 7, 11, 15]
target = 9
seen = {}

for i, n in enumerate(num):
    needed = target - n

    if needed in seen:
        print("Indexes:", seen[needed], i)
        break

    seen[n] = i
else:
    print("No pair found")
