n = 25

threshold = 0.001
approximation = n/2

while True:
    better = (approximation + n/approximation)/2
    print(better)
    if abs(approximation - better) < threshold:
        print(better)

#The program indefinitely outputs 7.25 as better...