'''Assignment 15: Average Speed for Multiple Trips

Write a Python program that:

Accepts distance1, time1, distance2, time2.
Calculates average speed.

Input:
Distance1 = 60
Time1 = 1
Distance2 = 40
Time2 = 1

Output:
Average Speed = 50 km/h'''

Distance1,Time1 = map(int,input("Enter Distance1 and Time1: ").split())
Distance2,Time2 = map(int,input("Enter Distance2 and Time2: ").split())

Average_Speed = int(Distance1+Distance2)/(Time1+Time2)

print(f"Average Speed = {Average_Speed}km/h")