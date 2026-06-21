"""Assignment 2: Salary Calculator

Write a Python program that:

Accepts daily wage and number of days.
Calculates total salary.

Input:
Daily wage = 500
Days = 26

Output:
Salary = 13000"""

Daily_wage = int(input("Enter Daily Wage: "))
Days = int (input("Enter Days: "))

Salary = (Daily_wage*Days)

print(f"Salary = {Salary}")