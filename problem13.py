balance = float(input("Enter your current balance: "))
withdraw = float(input("Enter withdrawal amount: "))

if withdraw <= 0:
    print("Invalid withdrawal amount")

elif withdraw > balance:
    print("Insufficient balance")

else:
    balance = balance - withdraw
    print("Withdrawal successful")
    print("Remaining balance:", balance)