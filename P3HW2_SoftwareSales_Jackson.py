# C-110
# P3HW2 - Software Sales
# Steven Jackson
# 6/26/2018

## Write a program that ask the user the number of packages purchased.
print("Welcome to our self-serve Kiosk!")
def main():
    
       

    # Get the number of packages purchased from the user.
    userNumberOfPackages = int(input("Enter the number of pac" + \
                                     "kages bought: "))

    # The retail price of a package is $99.    
    PackagePrice = 99
    # The discount for less than 10 packages is 0%.
    if userNumberOfPackages < 10:
            dicount = 0
    # The discount for 10-19 packages is 10%
    elif userNumberOfPackages >= 10 or userNumberOfPackages < 20:
            discount = 0.10
    # The discount for 20-49 packages is 20%
    elif userNumberofPackages >= 20 or userNumberOfPackages < 50:
            discount = 0.20
    # The discount for 50-99 packages is 30%
    elif userNumberOfPackages >= 50 or userNumberOfPackages < 100:
            discount = 0.30
    # The discount for 100+ packages is 40%
    else:
            discount = 0.40
            
    # Formula for the price of the packages.
    subTotal = userNumberOfPackages * PackagePrice
    # Formula for the discount of the packages.
    discountAmount = discount * subTotal
    # Formula for the final price of the packages.
    total = subTotal - discountAmount

    # Display the discount if any, non discounted price, total with discount.
    print("Amount of discount: $" + format(discountAmount, ",.3f" ) + \
          "\Total amount: $" + format(total, ",.2f" ))
    


main()
      

