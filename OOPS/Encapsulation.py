# 1: Bank account encapsulation
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance


account = BankAccount("Asha", 1000)
account.deposit(500)
account.withdraw(200)
print("Account balance:", account.get_balance())


# 2: Employee salary encapsulation
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Salary must be greater than zero")


employee = Employee("Ravi", 30000)
employee.set_salary(35000)
print(f"{employee.name}'s salary:", employee.get_salary())