amount = float(input("Enter the purchase amount (₹): "))

if amount > 5000:
    discount_percent = 20
elif amount >= 3000:
    discount_percent = 15
elif amount >= 1000:
    discount_percent = 10
else:
    discount_percent = 0

discount = amount * discount_percent / 100
final_amount = amount - discount

print("Discount:", discount_percent, "%")
print("Discount amount: ₹", discount)
print("Amount to pay: ₹", final_amount)