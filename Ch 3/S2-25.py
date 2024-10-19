numbers = [2, 5, 6, 8, 5, 7, 2, 1, -2, -19, 20, 21, 34, 23, 54]

total = []
for _ in numbers:
    if _ % 2 == 0:
        total.append(_)
    else:
        continue

final_total = sum(total)
print(final_total)
