starting_day = int(input("What is the starting day of your holiday? 1 is Sunday. Please enter a number from 1 to 7:  "))
days_away = int(input("How many days will your holiday last?"))
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

weeks = days_away // 7
return_day_nr = days_away % 7

day_text = days[starting_day -1]

print(day_text)