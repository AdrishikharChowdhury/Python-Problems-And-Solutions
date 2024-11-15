class Circle():
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return (22/7)*self.radius*self.radius
    def perimeter(self):
        return 2*(22/7)*self.radius
radius=float(input("Enter the radius of the circle: "))
circ=Circle(radius)
print("Area:",circ.area(),"\nPerimeter:",circ.perimeter())