num = int(input("Enter a number: "))

n = num
digit_sum = 0
digit_product = 1

while n > 0:
    digit = n % 10
    digit_sum += digit
    digit_product *= digit
    n //= 10

if digit_sum == digit_product:
    print(num, "is a spy number.")
else:
    print(num, "is not a spy number.")