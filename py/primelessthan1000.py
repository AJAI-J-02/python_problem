start=2

end=int(input("enter the range "))

for num in range(start,end):
    if num>1:
        prime=True
        
        for i in range(2,num):
            if num % i==0:
                prime=False
                break
    
    
        if prime:
            print(num,end =" ")
        