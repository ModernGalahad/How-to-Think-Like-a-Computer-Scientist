principal_amount = float(input("Please enter the principal amount:\n"))
annual_nominal_interest_rate = float(input("Please enter annual nominal interest rate (as a decimal):\n"))
n = float(input("Please enter the nr of times the interest is compounded in a year:\n"))
t = float(input("Please enter the number of years:\n"))

print("The final amount is: ",principal_amount * (1 + annual_nominal_interest_rate/n)**(n*t))