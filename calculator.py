print("This is the calculator program in Python:")
print("\n\n************CALCULATOR*************\n\n")
operator = int(input("Enter 1 for division\nEnter 2 for multiplication\nEnter 3 for subtraction\nEnter 4 for addition: "))
a = float(input("Enter number 1: "))
b = float(input("Enter number 2: "))

if operator == 1:
    print("Division is:", a / b)
elif operator == 2:
    print("Multiplication is:", a * b)
elif operator == 3:
    print("Subtraction is:", a - b)
elif operator == 4:
    print("Sum is:", a + b)
else:
    print("Invalid choice!")

