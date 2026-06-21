'''Assignment 8: Compound Interest

A person invests money in a bank that provides compound interest annually.

Input:
Principal = 10000
Rate = 5%
Time = 2 years

Expected Output:
Amount after interest = 11025.0'''

Principal = int(input("Enter the Principal amount = "))
Rate = int(input("Enter Rate of Intrest = "))
Time = int(input("Enter Time = "))

Intrest = Principal*(1+Rate/100)**2
print(f"Amount after intrest = {Intrest:.1f}")
