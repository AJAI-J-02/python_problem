num=int(input("enter the number "))
temp=num
digit=0
rev=0
while temp>0:
    digit=temp%10
    rev=rev*10+digit
    temp=temp//10

if num== rev :
    print(" is palindrom")
else:
    print("not palindrom")