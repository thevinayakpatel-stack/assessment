'''Assignment 12: Change Return System

Write a Python program that:

Accepts amount.
Calculates ₹100, ₹50, ₹10 notes.

Input:
Amount = 380

Output:
₹100 x 3
₹50 x 1
₹10 x 3'''

Amount = int(input("Enter Amount: "))

Hundread = int(Amount/100)
Fifty = int(Amount%100)//50
Ten = int(Amount%50)//10

print(f"₹100 * {Hundread}\n₹50 * {Fifty}\n₹10 * {Ten}")