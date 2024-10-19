numbers = [2, 5, 6, 8, 5, 7, 2, 1, 10]
odd_numbers = 0

for _ in numbers:
    if _ % 2 != 0:
        odd_numbers += 1
    else:
        continue

print(odd_numbers)


