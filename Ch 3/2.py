starting_day = int(input("What is the starting day of your holiday? 1 is Sunday. Please enter a number from 1 to 7:  ")) - 1
days_away = int(input("How many days will your holiday last?"))

days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

return_day = (days_away + starting_day) % 7

return_day_text = days[return_day]

print(return_day_text)

#3 ( wed) is starting day. I leave for 19 days. 