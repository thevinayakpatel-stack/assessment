
'''Assignment 7: Cricket Run Rate

In cricket, overs are given in decimal format (e.g., 48.3 means 48 overs and 3 balls). Convert overs into total balls and calculate run rate.

Input:
Total runs = 275
Overs = 48.3

Expected Output:
Total Balls = 291
Run Rate = 5.67'''

Total_runs = int(input("Enter Total runs = "))
Overs,balls = map(int,input("Enter Overs = ").split("."))

Balls = int(Overs*6)+balls
Run_Rate = (Total_runs*6)/Balls

print(f"Total Balls = {Balls}\nRun Rate = {Run_Rate:.2f}")