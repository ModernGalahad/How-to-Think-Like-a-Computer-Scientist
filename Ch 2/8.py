current_time = int(input("Current time (24h format, so for example 14 not 2 p.m.):\n"))
hours = int(input("Number of hours until the alarm goes off:\n"))
days = hours//24 
new_hour = (hours + current_time) % 24

print("In", days, "days at",new_hour)
 