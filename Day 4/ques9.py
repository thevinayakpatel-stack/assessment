'''Assignment 9: Petrol Cost Calculation

You traveled a certain distance. Based on mileage and petrol price, calculate fuel used and total cost.

Input:
Distance = 450 km
Mileage = 15 km/litre
Petrol price = 110/litre

Expected Output:
Petrol Used = 30.0 litres
Total Cost = 3300.0'''

Distance = int(input("Enter Distance = "))
Mileage = int(input("Enter Mileage = "))
Petrol_price = int(input("Enter Petrol Price = "))

Petrol_used = Distance / Mileage
Total_Cost = Petrol_used * Petrol_price

print(f"Petrol Used = {Petrol_used}litres\nTotal Cost = {Total_Cost}")