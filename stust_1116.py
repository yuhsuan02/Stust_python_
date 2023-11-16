class MyShape:
    def __init__(self,side,length,width,radius):
        self.side=side
        self.length=length
        self.width=width
        self.radius=radius

    def getSquareArea(self):
        return f"{self.side * self.side}"

    def getRectangleArea(self):
        return f"{self.length * self.width}"

    def getCircleArea(self):
        return f"{self.radius * self.radius * 3.14}"
        

p1= MyShape(20,30,40,50)
p2= MyShape(10,20,30,40)

print(p1.getSquareArea())
print(p1.getRectangleArea())
print(p1.getCircleArea())

print(p2.getSquareArea())
print(p2.getRectangleArea())
print(p2.getCircleArea())


