num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the Second number:"))
num3 = int(input("Enter the Third number:"))

if num1>num2 and num1>num3:
    print("The first number is the largest")
elif num2>num1 and num2>num3:
    print("The second number is the largest")
else:
    print("The third number is the largest")

