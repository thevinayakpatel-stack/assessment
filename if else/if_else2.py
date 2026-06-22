'''2. An e-commerce website provides discounts based on the cart value and user type.
The system should take cart value and user type (premium or regular) as input.
 If the cart value is greater than or equal to 5000, then check the user type. If the user is premium,
 apply a 20% discount; otherwise, apply a 10% discount. If the cart value is less than 5000,
then check if it is greater than or equal to 2000. If yes, apply a 5% discount; otherwise,
no discount is applied. Display the final payable amount.

Input:
Cart Value = 6000
User Type = Premium

Output:
Final Amount = 4800'''

cart_value = int(input("Enter cart Value: "))
user_type = input("Enter your type (premium/regular): ")

if cart_value>=5000:
   if user_type=="premium":
      print("final value with 20% discount is = ",(cart_value*80/100))
   else:
      print("final value with 10% discount is = ",(cart_value*90/100))
else:
     if cart_value>2000:
       print("final value with 5% discount is = ",(cart_value*95/100))
     else:
       print("final value",cart_value)