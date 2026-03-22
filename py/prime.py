num=int(input("enter the number "))

if num<=1:
    print("not prime")

    for i in range(2,num-1):
        if num%i==0:
            print("is not prime")
        
    else:
            print("prime ")
else :
    print("prime ")
    