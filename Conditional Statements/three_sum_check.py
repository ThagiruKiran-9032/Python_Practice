first = 4
second = 7
third = 9
target = 16

if first + second + third == target:
    print("The three values add up to the target")
elif first + second == target or first + third == target or second + third == target:
    print("Two values add up to the target")
else:
    print("No combination adds up to the target")