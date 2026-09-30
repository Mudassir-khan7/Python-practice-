amount = float(input("Enter total shopping amount: Rs. "))
premium = input("Are you a Premium Member? (Yes/No): ")

if amount >= 10000:
    discount_rate = 20
elif amount >= 5000:
    discount_rate = 10
elif amount >= 2000:
    discount_rate = 5
else:
    discount_rate = 0

regular_discount = amount * discount_rate / 100

premium_discount = 0

if premium == "Yes" or premium == "yes" or premium == "Y" or premium == "y":
    if amount > 0:
        premium_discount = amount * 5 / 100

total_discount = regular_discount + premium_discount
final_amount = amount - total_discount
print("\nOriginal Shopping Amount:", amount)
print("Regular Discount:", regular_discount)
print("Premium Discount:", premium_discount)
print("Total Discount:", total_discount)
print("Final Amount to Pay:", final_amount )