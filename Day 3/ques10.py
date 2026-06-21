'''Assignment 10: Percentage Calculator

Write a Python program that:

Accepts total marks and obtained marks.
Calculates percentage.

Input:
Total = 500
Obtained = 400

Output:
Percentage = 80%'''

Total = int(input("Enter Total Marks: "))
Obtained = int(input("Enter Obtained Marks: "))

Percentage = (Obtained/Total*100)

print(f"Percentage = {Percentage}%")