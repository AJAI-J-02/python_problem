class rectangle:
    def __init__(self,height,width):
        self.height=height
        self.width=width
        
    def area(self):
        return self.height*self.width
    def perimeter(self):
        return 2*(self.height+self.width)
    
r=rectangle(5,4)
print(r.area())
print(r.perimeter())