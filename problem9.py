num1 = int(input("Enter a number for check"))

if num1%5 == 0 and num1%11 == 0:
    print(" divisable by both 5 and 11 ")
elif num1%5 == 0:
    print(" Divisible by 5 ")
elif num%11 == 0:
    print(" Divisible by 11 ")
else:
    print(" Not divisible ")