"""Assignment 3: Electricity Bill Calculator

Write a Python program that:

Accepts number of units.
Calculates bill (₹6 per unit).

Input:
Units = 100

Output:
Bill = 600"""

Units = int(input("Enter Units: "))
Per_unit = 6

Bill = (Units*Per_unit)

print(f"Bill = {Bill}")