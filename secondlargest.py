num = []
for i in range(5):
    n = int(input("Enter a number: "))
    num.append(n)
print("List:",num)
largest = max(num)
num.remove(largest)
second_largest = max(num)
print("The second largest number is:", second_largest)