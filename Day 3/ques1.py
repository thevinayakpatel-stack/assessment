"""Assignment 1: Speed Calculator

Write a Python program that:

Accepts distance (in km) and time (in hours).
Calculates speed.

Input:
Distance = 120
Time = 2

Output:
Speed = 60 km/h"""

Distance = int(input("Enter the distance in km: "))
Time = int(input("Enter the time in hour: "))

Speed = int(Distance/Time)

print(f"Speed = {Speed} km/h")