total_duration = int(input("enter event duration in seconds ="))

hour = total_duration//3600
minute = (total_duration%3600)//60
remaning_seconds = total_duration%60

print("hour",hour,"\nminute",minute,"\nsecond",remaning_seconds)