num = int(input("Enter a number: "))
sum_digits = 0
product = 1
while num > 0:
    digit = num % 10
    sum_digits += digit
    product *= digit
    num //= 10
if sum_digits == product:
    print("Spy Number")
else:
    print("Not Spy Number")
