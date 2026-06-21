'''Assignment 4: Travel Distance Calculation

A person is traveling at a constant speed. Time is given in hours and minutes. Convert total time into hours and calculate distance.

Input:
Speed = 60 km/hr
Time = 2 hours 30 minutes

Expected Output:
Total Time = 2.5 hours
Distance = 150.0 km'''

Speed = int(input("Enter the Speed in km/hr= "))
hour,minutes = input("Enter the Time = ").split(.)

Total_Time = int(hour) + int(minutes)/60
Distance = Speed * Hour,minutes

print(f"Total Time = {Speed}\nDistance = {Distance}")



