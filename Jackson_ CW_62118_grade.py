# CW_62118_Grade
# Steven Jackson
# 6/21/2018
# Use the if/else structure to determine a letter grade

# Get input from the user

grade = int(input("Enter a numerical grade from 0 to 100:  "))


if grade > 89 and grade < 101:
    print ("You made an A!")
    print ("Your numeric grade of", grade, "is an A:")
elif grade > 79 and grade < 90:
    print ("You made an B!")
    print ("Your numeric grade of", grade, "is an B:")
elif grade > 69 and grade < 80:
    print ("You made an C!")
    print ("Your numeric grade of", grade, "is an C:")
elif grade > 59 and grade < 70:
    print ("You made an D!")
    print ("Your numeric grade of", grade, "is an D:")
elif grade >= 0 and grade <60:
    print ("You made an F!")
    print ("Your numeric grade of", grade, "is an F:")
else:
    print("Invalid input. Try again.")


    

