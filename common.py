n1 = int(input("How many numbers in list 1? "))
list1 = []
for i in range(n1):
    list1.append(int(input("Enter number: ")))

n2 = int(input("How many numbers in list 2? "))
list2 = []
for i in range(n2):
    list2.append(int(input("Enter number: ")))

common = []
for x in list1:
    if x in list2 and x not in common:
        common.append(x)

print("Common elements:", common)