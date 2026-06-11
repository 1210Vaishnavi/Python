num = int(input("Enter a number: "))
square = num * num
sum_digits = 0
while square > 0:
    sum_digits += square % 10
    square //= 10
if sum_digits == num:
    print("Neon Number")
else:
    print("Not Neon Number")
