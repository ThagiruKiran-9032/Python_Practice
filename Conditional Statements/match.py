choice = int(input("Enter your choice (1: Add, 2: Subtract, 3: Multiply, 4: Divide): "))
first_number = 20
second_number = 5

match choice:
    case 1:
        result = first_number + second_number
        operation = "1"
    case 2:
        result = first_number - second_number
        operation = "2"
    case 3:
        result = first_number * second_number
        operation = "3"
    case 4 if second_number != 0:
        result = first_number / second_number
        operation = "4"
    case 4:
        result = None
        operation = "division by zero"
    case _:
        result = None
        operation = "invalid choice"

if result is None:
    print("Cannot perform", operation)
else:
    print(operation.capitalize() + " result:", result)
