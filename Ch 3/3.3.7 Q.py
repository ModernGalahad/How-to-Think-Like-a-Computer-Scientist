n = 0
count = 0

while n > 0:
    digit = n % 10
    if digit == 0 or digit == 5:
        count = count + 1
    n = n//10

print(count)

#This did not print 1 because this is a while loop, with a condition of "n > 0". Python first tried to see if n > 0, and 
#because it wasn't, it stopped the program, and printed what was in the count variable, which is 0.