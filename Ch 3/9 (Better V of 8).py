side_a = float(input("Enter the dimensions of side a:  "))
side_b = float(input("Enter the dimensions of side b:  "))
side_c = float(input("Enter the dimensions of side c:  "))
threshold = 1e-7 

if side_a >= side_b and side_a >= side_c:
    hypotenuse = side_a
    leg_1 = side_b
    leg_2 = side_c
elif side_b >= side_a and side_b >= side_c:
    hypotenuse = side_b
    leg_1 = side_a
    leg_2 = side_c
else:
    hypotenuse = side_c
    leg_1 = side_a
    leg_2 = side_b

if abs(((leg_1 ** 2) + (leg_2 ** 2)) - (hypotenuse ** 2)) < threshold:
    print("This is a right triangle.")
else:
    print("This is not a right triangle.")

