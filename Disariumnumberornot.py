num = input("Enter a number: ")
total = 0
for i in range(len(num)):
    total += int(num[i]) ** (i + 1)
if total == int(num):
    print("Disarium Number")
else:
    print("Not a Disarium Number")
