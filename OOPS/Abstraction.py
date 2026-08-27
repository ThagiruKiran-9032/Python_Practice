from abc import ABC, abstractmethod

# 1: Shape abstraction
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

circle = Circle(5)
print("Circle area:", circle.area())


# 2: Payment abstraction
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid Rs. {amount} using credit card")

payment = CreditCardPayment()
payment.pay(1000)