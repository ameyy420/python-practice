year = int(input("Enter a number for check :"))
if year%4 ==0 and year%400 ==0:
    print("This is a leap year")
elif year%100 == 0:
    print("This year is not a leap year")
