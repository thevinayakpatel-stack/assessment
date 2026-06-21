'''Assignment 5: Salary Breakdown

An employee wants to calculate salary per day and per hour.

Input:
Monthly salary = 36000
Working days = 24
Working hours per day = 8

Expected Output:
Salary per day = 1500.0
Salary per hour = 187.5'''

Salary = int(input("Enter Monthly Salary = "))
Working_days = int(input("Enter Working Days = "))
Working_hour = int(input("Enter Working Hours = "))


Salary_days = Salary/Working_days
Salary_hour = Salary_days/Working_hour

print(f"Salary Per days = {Salary_days}\nSalary Per Hours = {Salary_hour}")