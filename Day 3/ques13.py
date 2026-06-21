'''Assignment 13: Compound Interest Calculator

Write a Python program that:

Accepts principal, rate, and time.
Calculates compound interest.

Input:
Principal = 1000
Rate = 10
Time = 2

Output:
Amount = 1210.0
Compound Interest = 210.0'''

Principal = int(input("Enter Principal: "))
Rate = int(input("Enter Rate: "))
Time = int(input("Enter Time: "))

Amount = int(Principal*(1+Rate/100)**Time)
CI = Amount-Principal

print(f"Amount ={Amount:.1f}\nCompound Intrest = {CI:.1f}")