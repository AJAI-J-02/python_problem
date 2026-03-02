a=int(input("enter the value of a :"))
b=int(input("enter the value of b :"))
LHS=(a+b)*(a+b)
RHS=a*a+2*a*b+b*b
if LHS==RHS :
    print(f" True  ,LHS {LHS}  and RHS {RHS}")
else:
    print(f" False  ,LHS {LHS}  and RHS {RHS}")