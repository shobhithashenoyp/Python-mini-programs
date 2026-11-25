num = int(input("Enter a number: "))
sum = 0
while num > 0:
    digit = num%10
    sum+=digit
    num//=10
print("The sum of digits is:", sum)
if sum%2==0:
    print("The sum of digits is even.")
else:
    print("The sum of digits is odd.")