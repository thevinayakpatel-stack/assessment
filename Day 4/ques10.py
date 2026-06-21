'''Assignment 10: Time Conversion

Convert total seconds into hours, minutes, and seconds.

Input:
Total seconds = 7384

Expected Output:
Hours = 2
Minutes = 3
Seconds = 4'''

Total_Seconds = int(input("Enter Total Seconds = "))

Hours = int(Total_Seconds/3600)
Minutes = int((Total_Seconds%3600)/60)
Seconds = int(Total_Seconds%60)

print(f"Hours = {Hours}\nMinutes = {Minutes}\nSeconds = {Seconds}")
