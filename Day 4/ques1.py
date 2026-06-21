'''Assignment 1: Restaurant Bill Split

A group of friends went to a restaurant. The restaurant adds GST and service charge to the bill, and then the total is divided equally.
g
Input:
Total bill amount = 2500
GST = 5%
Service charge = 10%
Number of friends = 4

Expected Output:
Final Bill = 2875.0
Each Person Pays = 718.75'''

Total_bill = int(input("Enter the Bill: "))
GST = int(input("Enter GST: "))
Service_charge = int(input("Enter Service Charge: "))
Persons = int(input("Enter Number of Person's: "))

Final_bill = 2500+(2500*5/100)+(2500*10/100)
Each_person = Final_bill/Persons

print(f"Final Bill ={Final_bill}\nEach Person's Pays = {Each_person}")