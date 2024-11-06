print("Welcome to the market! Please see our items below.")
print()
print("Bread \t\t $1.40/loaf")
print("Chicken \t $2.75/lb")
print("Chips \t\t $3.30/bag")
print("Cookies \t $2.60/box")
print()
print()
loafs = int(input("How many loafs of bread would you like? "))
chicken = int(input("How many pounds of chicken would you like? "))
chips = int(input("How many bags of chips would you like? "))
cookies = int(input("How many boxes of cookies would you like? "))
print()
print()
print("---------------------------------------------------------------")
print()
print()
print("Thank you for shopping with us! Please find your receipt below.")
cost_bread = round(loafs * 1.4, 2)
cost_chicken = round(chicken * 2.75, 2)
cost_chips = round(chips * 3.3, 2)
cost_cookies = round(cookies * 2.6, 2)
sub_total = cost_cookies + cost_chips + cost_chicken + cost_bread
tax_rate = 0.06
tax = round(tax_rate * sub_total, 2)
total = round(sub_total + tax, 2)

print()
print("Bread \t\t\t x" + str(loafs) + "\t\t\t" + f"${round(cost_bread, 2):,.2f}")
print("Chicken \t\t x" + str(chicken) + "\t\t" + f"${round(cost_chicken, 2):,.2f}")
print("Chips \t\t\t x" + str(chips) + "\t\t\t" + f"${round(cost_chips, 2):,.2f}")
print("Cookies \t\t x" + str(cookies) + "\t\t\t" + f"${round(cost_cookies, 2):,.2f}")
print()
print()
print("Sub Total: \t\t\t\t " + f"${round(sub_total, 2):,.2f}")
print("Tax: \t\t\t\t\t " + f"${round(tax, 2):,.2f}")
print()
print("Total: \t\t\t\t\t " + f"${round(total,2):,.2f}")
print()
print("---------------------------------------------------------------")
