numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]

#a) and b)

for _ in numbers:
    sqrt_1 = _ ** 0.5
    print("The square root of", _, "is", sqrt_1)

#c) 
total = 0
for _ in numbers:
    total += _ 

print("This is", total)

#d)
product = 1
for _ in numbers:
    product *= _

print(product)