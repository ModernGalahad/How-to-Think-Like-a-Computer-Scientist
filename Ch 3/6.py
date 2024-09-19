grades = [ 83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]
text_grades = [ ]
for _ in grades:
    if _ >=  75:
        text_grades.append("First")
    elif 70 <= _ < 75:
        text_grades.append("Upper Second")
    elif 60 <= _ < 70:
        text_grades.append("Second")
    elif 50 <= _ < 60:
        text_grades.append("Third")
    elif 45 <= _ < 50:
        text_grades.append("F1 Supp")
    elif 40 <= _ < 45:
        text_grades.append("F2")
    elif _ < 40: 
        text_grades.append("F3")


print(text_grades)

