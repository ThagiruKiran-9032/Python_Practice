num = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
current_sum = num[0]
maximum_sum = num[0]

for n in num[1:]:
    current_sum = max(n, current_sum + n)
    maximum_sum = max(maximum_sum, current_sum)

print("Maximum subarray sum:", maximum_sum)
