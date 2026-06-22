'''1. A bank wants to automate its loan approval process. The system should take salary,
credit score, and number of existing loans as input. If the salary is greater than or equal to 30000,
then it should check the credit score. If the credit score is greater than or equal to 750,
 the loan should be approved. Otherwise, it should check the number of existing loans.
If the existing loans are less than 2, the loan should be conditionally approved; otherwise, it should be rejected.
If the salary is less than 30000, the loan should be rejected. Display the final loan status.

Input:
Salary = 40000
Credit Score = 720
Existing Loans = 1'''

salary = int(input("Enter Salary amount: "))
credit_score = int(input("Enter Credit score: "))
existing_loans = int(input("Enter Existing loans: "))

if salary>=30000:
     if credit_score>=750:
         print("loan is approved")
     else:
         if existing_loans<2:
            print("loan is conditionally approved")
         else :
            print("existing value is high.")
else:
     print("Salary is low")        
