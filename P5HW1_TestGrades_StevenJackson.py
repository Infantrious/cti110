#CTI-110
#P5HW1 - Test Average and Grade
#Steven Jackson
#7/10/18


#Write a program that asks the user to enter five test grades.

#get the grade from the user.
def main():

    grade1, grade2, grade3, grade4, grade5 = askforGrades()
##    determine_grades
    calc_average(grade1, grade2, grade3, grade4, grade5)
    printresults(grade1, grade2, grade3, grade4, grade5) 


#get the grades from user.
def askforGrades():
    grade1 = float(input(" Enter first test grade: "))
    grade2 = float(input(" Enter first test grade: "))
    grade3 = float(input(" Enter first test grade: "))
    grade4 = float(input(" Enter first test grade: "))
    grade5 = float(input(" Enter first test grade: "))

    return grade1, grade2, grade3, grade4, grade5

#show letter grades.
def determine_grade(user_grade):
    if(user_grade < 60):
        return "F"
    elif(user_grade < 70):
        return "D"
    elif(user_grade < 80):
        return "C"
    elif(user_grade < 90):
        return "B"
    elif(user_grade < 101):
        return "A"

#average up the grades.
def calc_average(grade1, grade2, grade3, grade4, grade5):
    average =(grade1 + grade2 + grade3 + grade4 + grade5)/5
    print("Your average is", average )
    
    

#display grades
def printresults(grade1, grade2, grade3, grade4, grade5):
    print("Grade\tLetter Grade")
    print(str(grade1) + "\t" + str(determine_grade(grade1)), \
          str(grade2) + "\t" + str(determine_grade(grade2)), \
          str(grade3) + "\t" + str(determine_grade(grade3)), \
          str(grade4) + "\t" + str(determine_grade(grade4)), \
          str(grade5) + "\t" + str(determine_grade(grade5)))

#call main   
main()         

