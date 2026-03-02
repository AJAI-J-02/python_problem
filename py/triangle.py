
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if a >= b and a >= c:
    hyp = a
    side1 = b
    side2 = c
elif b >= a and b >= c:
    hyp = b
    side1 = a
    side2 = c
else:
    hyp = c
    side1 = a
    side2 = b

if hyp * hyp == side1 * side1 + side2 * side2:
    print("The triangle is a right-angled triangle")
else:
    print("The triangle is NOT a right-angled triangle")