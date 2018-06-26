# CTI-110
# P3LAB 
# Steven Jackson
# 6/26/18 

def main():
# This program takes a number grade and outputs a letter grade.
# This program uses 10-point grading scale. 90-100(A), 80-89(B),70-79(C),60-69(D,
# 0-59(F)
    grade = int(input("Enter a numeric grade from 0 to 100: "))

    if grade > 89 and grade < 100:
        print("You made an A!")
        
    elif grade > 79 and grade < 90:
        print("You made an B!")
        
    elif grade > 69 and grade < 80:
        print("You made an C!")
        
    elif grade > 59 and grade < 70:
        print("You made an D!")
        
    elif grade >= 0 and grade < 60:
        print("You made an F!")
        
    else:
        print("Invalid input. Try again")

    

main()
