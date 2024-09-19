
print("Please give me the length of two sides of a right triangle:")
side_1 = float(input("Side 1:  "))
side_2 = float(input("Side 2:  "))

hypotenuse = ((side_1 ** 2) + (side_2 ** 2)) ** 0.5

print("The length of the hypotenuse is " + str(hypotenuse))