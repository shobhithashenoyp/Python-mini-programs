num = []
pos = []
neg = []
zero = []
for i in range(10):
    n=int(input("Enter a number: "))
    num.append(n)
    if n>0:
        pos.append(n)
    elif n<0:
        neg.append(n)
    else:
        zero.append(n)
print("List:",num)
print("Positive numbers:",pos)
print("Negative numbers:",neg)
print("Zero numbers:",zero)