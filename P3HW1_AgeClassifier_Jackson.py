# CTI-110 
# P3HW1 - Age Classifier 
# Steven Jackson 
# 6/26/2018

##Write a program that asks the user to enter a person's age.

# Get input from the user
def main():
    def classifier():
        print("Happy aging!")

    age = int(input("Enter your age, or someone else's age: "))
    #If the person is 1 year old or less, he or she is an infant.
    if age <= 1:
        print("Goo-goo, Gaa-gaa!")
        print("You are an infant!")
    #If the person is older that 1 year, but younger than 13 years old, he or she is a child.
    elif age < 13:
        print("Do you wanna build a snowman!")
        print("You are a child!")
    #If the person is at least 13 years old, but less than 20 years old, he or she is a teenager
    elif age < 20:
        print("Parents Just Don't Understand!")
        print("You are a teenager!")
    #If the person is at least 20 years old, he or she is an adult.
    elif age >= 20 and age <= 117:
        print("If you could just be a child again!")
        print("You are an adult!")
    elif age >117:
        print("Woooooooooooooah!")
        print("You are a fossil!")              
    
    classifier()
    restart = input("Do you want to run this program again? Enter yes to continue: ") 
    if restart == "yes":
        main()
    else:
        print("Age ain't nothing but a number, Goodbye!")
        exit()
        
main()
                
    


