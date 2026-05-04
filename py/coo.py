r =int(input("enter the range "))
even=0
odd=0
for i in range(r):
    num = int(input("Enter number: "))
    if num%2==0:
        even=even+1
        
    else:
        odd=odd+1
       
print("even numbers ",even)      
print("odd numbers",odd)