'''Assignment 2: Mobile EMI Calculation

You purchased a mobile phone using EMI. After paying a down payment, the remaining amount includes interest and is divided into monthly installments.

Input:
Mobile price = 30000
Down payment = 5000
Interest rate = 10%
Months = 10

Expected Output:
Remaining Amount = 25000
Total with Interest = 27500
Monthly EMI = 2750.0'''

Mobile_price = int(input("Enter Mobile Price: "))
Down_payment = int(input("Enter Down Payment: "))
Intrest_rate = int(input("Enter Intrest rate: "))
Months = int(input("Enter Months: "))

Remaining_Amount = (Mobile_price - Down_payment)
Total_with_intrest = Remaining_Amount + (Remaining_Amount * Intrest_rate/100)
Monthly_EMI = (Total_with_intrest/Months)

print(f"Remaining Amount ={Remaining_Amount}\nTotal with Intrest ={Total_with_intrest}\nMonthly EMI = {Monthly_EMI}")