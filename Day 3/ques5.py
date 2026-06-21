"""Assignment 5: Average Marks Calculator

Write a Python program that:

Accepts marks of 3 subjects.
Calculates average.

Input:
Marks = 80, 90, 70

Output:
Average = 80.0"""

Hindi,English,Maths = map(int,input("Enter Marks: ").split())

Average = (Hindi+English+Maths)/3

print(f"Average = {Average}")