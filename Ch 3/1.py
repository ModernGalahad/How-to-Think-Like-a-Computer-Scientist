days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

day_num = int(input("Enter a day number (1-7): "))
new_num = day_num - 1

if 0 <= new_num <= 6:
    print("The day is " + days[new_num])
else:
    print("Invalid day number! Please enter a number between 0 and 6.")
