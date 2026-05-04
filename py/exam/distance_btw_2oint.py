import math
p1=int(input("enter the x1 "))
p2=int(input("enter the x2 "))
p3=int(input("enter the y1 "))
p4=int(input("enter the y2 "))

#equation

y=0
x=0
y=p4-p3
x=p2-p1

m=math.sqrt((p2 - p1)**2 + (p4 - p3)**2)

print(" the point is :",m)
