def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return discount_percent
    else:
        return price

# Prompting user for input
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculating final price
final_price = calculate_discount(price, discount_percent)

# Output
if final_price == price:
    print("No discount applied. Final price:", final_price)
else:
    print("Final price after applying discount:", final_price)
