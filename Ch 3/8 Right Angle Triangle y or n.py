side_a = float(input("Enter the dimensions of side a:  "))
side_b = float(input("Enter the dimensions of side b:  "))
side_c = float(input("Enter the dimensions of the hypotenuse:  "))
threshold = 1e-7 

if abs(((side_a ** 2) + (side_b ** 2)) - (side_c ** 2)) < threshold:
    print("This is a right triangle.")
else:
    print("This is not a right triangle.")

