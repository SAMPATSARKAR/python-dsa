# lst1=[1,2,3,4]
# lst2=["a","b","c","d"]
# pair=list(zip(lst1,lst2))
# print(pair)

# numbers=[1,2,3,4,5,6,7,8,9]

# list(map(square,numbers))
##Polymorphism with Function and Methods 
##Base class

class Rectangle(Shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height 

    def area(self):
        return self.width * self.height
# DErived class 2
class Circle(Shape):
    def __init__(self,radius): 
        self.radius=radius 
    def area(self):
        return 3.14*self.radius*self.radius 
#Function that demonstrate polymorphism 
def print_area(shape):
    print(f"the area is {shape.area()}")
rectangle = Rectangle(4,5)
circle=Circle(2)

print_area(rectangle)
print_area(circle)

