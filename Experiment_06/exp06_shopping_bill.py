# Data
prices = [60, 30, 40]
quantities = [2, 3, 2]
discount_rate = 10
tax_rate = 5

# Code
subtotal = sum(p * q for p, q in zip(prices, quantities))
discount = subtotal * discount_rate / 100
amount = subtotal - discount
tax = amount * tax_rate / 100
total = amount + tax

print("Subtotal:", subtotal)
print("Discount:", discount)
print("Tax:", tax)
print("Total Cost:", total)
