num = int(input("Enter a number: "))
square = num * num
if str(square).endswith(str(num)):
    print("Automorphic Number")
else:
    print("Not Automorphic Number")
