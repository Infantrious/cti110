# CTI-110
# P3T1 - Areas of Rectangles
# Steven Jackson
# 6/26/18
 
 
## Write a program that asks for the length and width of two Rectangles.

print("This program will calculate the area of two rectangles.")
print("Calculate the area of the first rectangle.")
# Define the first rectangle and the second rectangle.
               
def area_1():
        length = int(input("Enter the length of first rectangle: "))
        width = int(input("Enter the width of first rectangle: "))
# Area = L * W        
        area = length * width
# Give the answer
        print("The area of the first rectangle is:", area)              
        return area
             

def area_2():
        length = int(input("Enter the length of second rectangle: "))
        width = int(input("Enter the width of second rectangle: "))
# Area = L * W
        area = length * width
# Give the answer
        print("The area of the second rectangle is:", area) 
        return area

first_rectangle_area = area_1()
print("Now calculate the area of the second rectangle.")
second_rectangle_area = area_2()
if first_rectangle_area > second_rectangle_area:
	print("The first rectangle has the larger area.")
elif first_rectangle_area < second_rectangle_area:
	print("The second rectangle has the larger area.")
else:
    print("Both Rectangles have equal area.")
