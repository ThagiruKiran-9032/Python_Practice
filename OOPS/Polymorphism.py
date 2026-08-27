# 1: Method overriding
class Animal:
    def speak(self):
        print("Animal makes a sound")


class Dog(Animal):
    def speak(self):
        print("Dog says: Woof!")


class Cat(Animal):
    def speak(self):
        print("Cat says: Meow!")


animals = [Dog(), Cat()]
for animal in animals:
    animal.speak()


# 2: Same method used for different shapes
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


shapes = [Circle(5), Rectangle(4, 6)]
for shape in shapes:
    print("Area:", shape.area())