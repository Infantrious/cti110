#CTI-110
#P5T2 - Feet To Inches
#Steven Jackson
#7/10/18

# Number of inches per foot.
INCHES_PER_FOOT = 12

# main function
def main():
    # Get the number of feet from the user.
    feet = int(input("Enter a number of feet: "))

    # Convert feet too inches.
    print(feet, "equals", feet_to_inches(feet), "inches.")

# feet to inches conversion function
def feet_to_inches(feet):
    return feet *INCHES_PER_FOOT

inches =feet_to_inches(1)

# call the main function.
main()
