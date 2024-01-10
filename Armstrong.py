n = input("Enter number:")
s = list(n)
newN = 0
for i in s:
    newN = int(i) * int(i) * int(i) + newN
if (newN == int(n)):
    print("It is an Armstrong Number")
else:
    print("It is not an Armstrong Number")

