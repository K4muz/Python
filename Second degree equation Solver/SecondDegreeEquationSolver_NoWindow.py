import math

#second degree equation py
a = input("a: ")
b = input("b: ")
c = input("c: ")

b2 = int(b) * int(b)
delta = b2 - 4 * int(a) * int(c)
if delta < 0:
    print("No real solutions")
else:
    if delta >= 0:
        root = math.sqrt(int(delta))
        bhaskara1 = (- int(b) + int(root)) / 2*int(a)
        bhaskara2 = (- int(b) - int(root)) / 2*int(a)
        print("The answer is: ", "x1= ",int(bhaskara1), "and x2= ",int(bhaskara2))