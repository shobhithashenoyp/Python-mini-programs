n = int(input("How many numbers? "))
numbers = []
for i in range(n):
    numbers.append(int(input("Enter number: ")))

non_zeros = []
zero_count = 0

for x in numbers:
    if x == 0:
        zero_count += 1
    else:
        non_zeros.append(x)

result = non_zeros + [0] * zero_count

print("Original list:", numbers)
print("Updated list :", result)