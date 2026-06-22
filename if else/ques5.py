'''5. Banking Security System
   A bank validates login attempt:

* If username is "admin" → Valid user
* If password length ≥ 8 → Strong password

Input:
Enter username: admin
Enter password: secure123

Output:
Valid user
Strong password'''

username = input("Enter username : ")
password = input("Enter password : ")

if username=="admin":
        if len(password)>=8:
             print("Valid user\nStrong password")
        else:
             print("Valid user\nWeak password")
else:
    print("invalid user")