# 01

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} says hello!")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def bark(self):
        print(f"{self.name} barks!")


d1 = Dog("Rex")
d1.speak()
d1.bark()


# 02

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} vehicle starts")


class Car(Vehicle):
    def drive(self):
        print(f"{self.brand} car is driving")


car = Car("Toyota")
car.start()
car.drive()

