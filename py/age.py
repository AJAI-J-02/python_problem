person1=int(input("enter the age p1 :"))
person2=int(input("enter the age p2 :"))
person3=int(input("enter the age p3 :"))
if person1 >= person2 and person1 >= person3:
    eldest = person1
elif person2 >= person1 and person2 >= person3:
    eldest = person2
else:
    eldest = person3
    
if person1 <= person2 and person1 <= person3:
    youngest = person1
elif person2 <= person1 and person2 <= person3:
    youngest = person2
else:
    youngest = person3

# Output results
print("Eldest age:", eldest)
print("Youngest age:", youngest)

