'''8. A warehouse management system needs to identify the highest stock level among six different storage units to prioritize dispatch.
 The system should take the quantity of items stored in six units as input. It should compare all six values using nested conditions
 and determine which unit has the maximum stock. Display the highest stock value among all six units.

Input:
Unit1 = 120
Unit2 = 450
Unit3 = 300
Unit4 = 275
Unit5 = 500
Unit6 = 390

Output:
Highest Stock = 500'''

unita1 = int(input("Enter stock of Unit 1: "))
unitb2 = int(input("Enter stock of Unit 2: "))
unitc3 = int(input("Enter stock of Unit 3: "))
unitd4 = int(input("Enter stock of Unit 4: "))
unite5 = int(input("Enter stock of Unit 5: "))
unitf6 = int(input("Enter stock of Unit 6: "))

if  unita1 > unitb2:
   if unita1 > unitc3:
      if unita1 > unitd4:
         if unita1 > unite5:
               if unita1 > unitf6:
                  print("highstock is a1 = ",unita1)
               else:
                  print("highstock is f6 = ",unitf6)
         else:
               if unite5 > unitf6:
                  print("highstock is e5 = ",unite5)
               else:
                  print("highstock is f6 = ",unitf6)
      else: 
          if unitd4 > unite5:
             if unitd4 > unitf6:
                print("highstock is d4",unitd4)
             else:
                print("highstock is f6",unitf6)
          else:
             if unite5 > unitf6:
                print("highstock is e5",unite5)
             else:
                print("highstock is f6",unitf6)
   else:
    if unitc3 > unitd4:
      if unitc3 > unite5:
         if unitc3 > unitf6:
            print("highstock is c3",unitc3)
         else:
            print("highstock is f6",unitf6)
      else:
         if unite5 > unitf6:
            print("highstock is e5",unite5)
         else:
            print("highstock is f6",unitf6)
    else:
       if unitd4 > unite5:
         if unitd4 > unitf6:
           print("highstock is unitd4",unitd4)
         else:
           print("highstock is unitf6",unitf6)
       else:
         if unite5 > unitf6:
           print("highstock is e5",unite5)
         else:
           print("highstock is f6",unitf6)
else: 
 if unitb2 > unitc3:
   if unitb2 > unitd4:
     if unitb2 > unite5:
       if unitb2 > unitf6:
          print("highstock is b2",unitb2)
       else:
          print("highstock is f6",unitf6)
     else:
       if unite5 > unitf6:
         print("highstock is e5",unite5)
       else:
         print("highstock is f6",unitf6)
   else:
     if unitd4 > unite5:
       if unitd4 > unitf6:
         print("highstock is d4",unitd4)
       else:
         print("highstock is f6",unitf6)
     else:
       if unite5 > unitf6:
         print("highstock is e5",unite5)
       else:
         print("highstock is f6",unitf6)
 else:
   if unitc3 > unitd4:
     if unitc3 > unite5:
       if unitc3 > unitf6:
          print("highstock is c3",unitc3)
       else:
          print("highstock is f6",unitf6)
     else:
       if unite5 > unitf6:
         print("highstock is e5",unite5)
       else:
         print("highstock is f6",unitf6)

   else:
      if unitd4 > unite5:
        if  unitd4 > unitf6:
          print("highstock is d4",unitd4)
        else:
          print("highstock is f6",unitf6)
      else:
        if unite5 > unitf6:
          print("highstock is e5",unite5)
        else:
          print("highstock is f6",unitf6)