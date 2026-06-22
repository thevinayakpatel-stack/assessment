'''3. E-Commerce Offer Engine
   An online store provides multiple offers independently:

* If cart value ≥ 500 → Free delivery
* If cart value ≥ 1000 → 10% discount coupon

Input:
Enter cart value: 1200

Output:
Free delivery applied
Discount coupon unlocked'''

value = int(input("Enter cart value :"))

if value>=500:
      if value>=1000:
         print("Free Delivery\ndiscount coupon  unlocked")
      else:
         print("Free Delivery\nDiscount coupon not unlocked")
else:
   print("Free delivery not applied")