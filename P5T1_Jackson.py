#CTI-110
#P5T1 - Kilometer Conversion
#Steven Jackson
#7/10/18


#Write a program that asks the user to enter a distance in kilometers, and then converts that distance to miles.

def main():
#Get the distance in kilometers.
    kilometers =float(input("Enter a distance in kilometers: "))

#Display the distance converted to miles.
    show_miles(kilometers)

def show_miles(km):
#calculate miles
    CONVERSION_FACTOR = 0.6214
    miles = km * CONVERSION_FACTOR

#Display the miles.
    print(km, "kilometers equals", miles, "miles.")

#Call the main function.

main ()
    
