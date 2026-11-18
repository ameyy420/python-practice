#User-এর কাছ থেকে একটি সংখ্যা নিয়ে তার নামতা Print করো।
n = int(input("Enter a number:"))
multi = 0

for i in range (n,11):
    multi = n*i
    print(n, "x", i, "=", n * i)
