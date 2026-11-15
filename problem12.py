num1 = int(input("Enter a number for check :"))
num2 = int(input("Enter a number for check :"))
operator = input("Enter an operator (+, -, *, /): ")

if operator == "+":
    result1 = num1 + num2
    print("Result of addition:", result1)
elif operator == "-":
    result2 = num1 - num2
    print("Result of subtraction:", result2)
elif operator == "*":
    result3 = num1 * num2
    print("Result of multiplication:", result3)
elif operator == "/":
    if num2 != 0:
        result4 = num1 / num2
        print("Result of division:", result4)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Error: Invalid operator.")