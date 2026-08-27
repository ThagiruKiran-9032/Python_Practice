class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    return "Hello my name is " + self.name + "\n" + "My age is " + str(self.age)

p1 = Person("John", 36)
print(p1.myfunc())