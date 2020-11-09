import turtle

s = turtle.getscreen()
t = turtle.Turtle()


class shape:
    def __init__(self, sides = 0, length = 0) :
        self.sides = sides
        self.length = length


class polygon(shape):
    def info(self):
        print("A polygon can be defined as a two dimensional plane with straight sides.")
        
class circle:
    def __init__(self, radius=0):
        self.radius = radius
    def show(self):
        t.circle(self.radius)

class triangle(polygon):
    def show(self):
        t.forward(self.length) 
        t.left(120)
        t.forward(self.length)
        t.left(120)
        t.forward(self.length)

class square(polygon):
    def show(self):
        t.fd(self.length)
        t.rt(90)
        t.fd(self.length)
        t.rt(90)
        t.fd(self.length)
        t.rt(90)
        t.fd(self.length)
        t.rt(90)

class pentagon(polygon):
    def show(self):
        for i in range(5):
           t.forward(self.length) 
           t.right(72) 

class hexagon(polygon):
    def show(self):
        for i in range(6):
           t.forward(self.length) 
           t.right(60)

class octagon(polygon):
    def show(self):
        for i in range(8):
           t.forward(self.length) 
           t.right(45)


sqr = square(4, 300)
sqr.info()
sqr.show()

cir = circle(100)
cir.show()

octa = octagon(8, 100)
octa.info()
octa.show()

tri = triangle(3, 200)
tri.info()
tri.show()





