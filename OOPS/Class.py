class MyClass:
    x = 5
p1 = MyClass()
p2 = MyClass()
p3 = MyClass()
del(p2)
print(p1.x)
print(p3.x)
