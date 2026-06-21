'''Assignment 9: Fuel Cost Calculator

Write a Python program that:

Accepts distance (km), mileage (km/litre), and petrol price.
Calculates total fuel cost.

Input:
Distance = 100
Mileage = 20
Petrol Price = 100

Output:
Cost = 500'''

Distance = int(input("Enter Distance: "))
Mileage = int(input("Enter Mileage: "))
Petrol_Price = int(input("Enter Petrol Price: "))

Cost = int(Distance/Mileage*Petrol_Price)

print(f"Cost ={Cost}")