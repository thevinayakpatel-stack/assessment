'''Assignment 8: Data Storage Converter

Write a Python program that:

Accepts value in MB.
Converts into GB.

Input:
MB = 2048

Output:
GB = 2.0'''

MB = int(input("Enter MB: "))

GB = MB/1024
print(f"GB ={GB:.1f}")