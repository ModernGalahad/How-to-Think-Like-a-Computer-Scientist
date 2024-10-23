numbers = [1, 5, 3, 7, 19, -1, 27, 4, 3, 9]

total_list = []
for _ in numbers:
    if _ % 2 != 0:
        total_list.append(_)
    else: break

total = sum(total_list)
print(total)