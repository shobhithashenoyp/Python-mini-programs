def even_digit_sum(n):
    total = 0
    while n > 0:
        digit = n % 10
        if digit % 2 == 0:
            total += digit
        n //= 10
    return total

num = int(input("Enter a number: "))
print("Sum of even digits:", even_digit_sum(num))