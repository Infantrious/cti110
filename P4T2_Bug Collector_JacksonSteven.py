# CTI-110
# P4T2 - Bug Collector
# Steven Jackson
# 7/2/18

# Write a program to help entomologist with their studies.
# Number of days the bugs were collected.
TotalDaysCollected = 7
# Number of bugs collected.
TotalNumberofBugs = 0
# Current day collection of bugs.
for currentDay in range(1, TotalDaysCollected + 1):
    bugsCollected = int(input("How many bugs were collected on today " + \
                              str(currentDay) + ":"))
    TotalNumberofBugs += bugsCollected
print("The total number of bugs collected for all", TotalDaysCollected, "days is:", \
      TotalNumberofBugs)
                              
                        
