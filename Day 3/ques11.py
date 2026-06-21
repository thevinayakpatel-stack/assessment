'''Assignment 11: Time Duration Adder

Write a Python program that:

Accepts hours, minutes, seconds.
Converts into total seconds.

Input:
Hours = 1
Minutes = 2
Seconds = 30

Output:
Total Seconds = 3750'''

Hours = int(input("Enter Hours: "))
Minutes = int(input("Enter Minutes: "))
Seconds = int(input("Enter Seconds: "))

Total_Seconds = (Hours*3600)+(Minutes*60)+(Seconds)

print(f"Total Seconds = {Total_Seconds}")
