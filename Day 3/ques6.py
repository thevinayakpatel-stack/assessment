'''Assignment 6: Discount Calculator

Write a Python program that:

Accepts total amount.
Calculates 10% discount and final price.

Input:
Amount = 1000

Output:
Discount = 100
Final = 900'''

Amount = int(input("Enter Amount: "))

Discount = int(Amount*10/100)
Final = int(Amount-Discount)

print(f"Discount = {Discount}")
print(f"Final = {Final}")