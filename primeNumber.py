n = int(input("Enter number:"))
for i in range(2, int(n / 2) + 1):
    if (i == n):
        continue
    else:
        if n % i == 0:
            print("It is not a Prime Number")
            break
else:
    print("It is a Prime Number")

