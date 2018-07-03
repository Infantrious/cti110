# CTI-110
# P4HW1 - Distance Travelled
# Steven Jackson
# 7/2/18

# Write a program that ask the user two questions.
# What is the speed of a vehicle? What is the number hours the vehicle has traveled.

# Get the speed of the vehicle.
SpeedofVehicle = float(input("What is the speed that the vehicle is travelling in mph?: "))
# Get how may hours the vehicle has traveled for.
HoursTraveled = int(input("How may hours has the vehicle been traveling for?: "))
# Display the speed of the vehicle and the hours traveled.
print("Hour", '\t',"Distance Traveled")
print("------------------------------")
for CurrentHour in range(1, HoursTraveled + 1):
    DistanceTraveled = SpeedofVehicle * CurrentHour
    print(CurrentHour, '\t', DistanceTraveled)
