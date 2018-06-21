# CW61918 Roman Numerals
# Steven Jackson
# 6/19/2018

## Convert integers 1 to 5 to Roman Numerals
# Create an integer variable to hold input from the user
# Give the user a prompt
choice = "y"
while choice == "y":
    
    number = int(input("Enter an integer (1 thru 5): "))

    if number == 1:
        print("I")
    elif number == 2:
        print("II")
    elif number == 3:
        print("III")
    elif number == 4:
        print("IV")
    elif number == 5:
        print("V")
    else:
        print("Invalid number")
    choice = input("Do you want to run the program again? Enter y for yes or n for no: ")
print("Goodbye")
    
##    if number == 1:
##        print("I")
##    else:
##        if number == 2:
##            print("II")
##        else:
##            if number == 3:
##                print("III")
##            else:
##                if number == 4:
##                    print("IV")
##                else:
##                    if number == 5:
##                        print("V")
##                    else:
##                        print("Invalid number")
##    choice = input("Do you want to run the program again? Enter y for yes or n for no: ")
##print("Goodbye")



