# CTI-110
# P2HW2 - Tip Tax Total
# Steven Jackson
# 6/17/2018

# Write a program that calculates the total cost of a meal purchased at a restaurant.

# Get the charge for the food from the user
foodCost = float(input("Input the price of your meal $: "))

# Tip amount
tipAmount = float(".18")
## Calculate tip amount
tipAmount = foodCost * tipAmount                        
# Display tip amount
print ("Tip amount is $: " "{0:.2f}".format(tipAmount))

# Sales Tax Amount

salesTax = float(".07")
## Calculate sales tax amount
salesTax = foodCost * salesTax
# Display sale tax amount
print ("Sales Tax amount is $: " "{0:.2f}".format(salesTax))

# Total cost of meal
totalCost = float                       
## Calculate the total cost of meal
totalCost = foodCost + tipAmount + salesTax
# Display total cost of meal
print ("Total Cost of meal is $: " "{0:.2f}".format(totalCost))
