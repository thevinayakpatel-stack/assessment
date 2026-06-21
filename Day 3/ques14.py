'''Assignment 14: Simple Profit or Loss Calculator

Write a Python program that:

Accepts cost price and selling price.
Calculates profit/loss and percentage.

Input:
Cost Price = 1000
Selling Price = 1200

Output:
Profit = 200
Profit % = 20.0'''

Cost_Price = int(input("Enter Cost Price: "))
Selling_Price = int(input("Enter Selling Price: "))

Profit = Selling_Price-Cost_Price
Percantage = (Profit/Cost_Price*100)

print(f"Profit = {Profit}\nProfit% = {Percantage}")