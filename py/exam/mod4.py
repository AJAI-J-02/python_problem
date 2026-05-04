import abs from ABC,abstractmethod
import math

class shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def circumference(self):
        pass
    
class circle(shape):
    def _init_(self,radius):
        self.radius=radius
        
    def area(self):
        return math.pi*self.radius**2
    
    def circumference(self):
        return 2*math.pi*self.radius
    
class rectangle(shape):
    
    def _init_(self,len,bre):
        self.len=len
        self.bre=bre
        
    def area(self):
        return self.len*self.bre
    
    def circumference(self):
        return 2*(self.len+self.bre)
    
    
c=circle(6)
r=rectangle(5,4)
print("Circle Area:", c.area())
print("Circle Circumference:", c.circumference())