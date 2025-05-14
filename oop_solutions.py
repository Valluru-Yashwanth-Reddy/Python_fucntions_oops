# Easy - 1
class Rectangle:
    def __init__(self, width, height):
       self.width = width
       self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width+self.height)
rect = Rectangle(5, 10)
print(rect.area())
print(rect.perimeter())

# Easy - 2

class Counter:
    def __init__(self):
        self.value = 0
    def increment(self):
        self.value += 1
    def decrement(self):
        self.value -= 1
    def reset(self):
        self.value = 0
# Example usage:
counter = Counter()
counter.increment()
counter.increment()
print(counter.value)  # Should return 2
counter.decrement()
print(counter.value)  # Should return 1
counter.reset()
print(counter.value)  # Should return 0


# Medium - 1

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
class Car(Vehicle):
    def __init__(self, make, model, year, doors, fueltype):
        super().__init__(make, model, year)
        self.doors = doors
        self.fueltype = fueltype
# Example usage:
car = Car("Toyota", "Corolla", 2020, 4, "Gasoline")
print(car.make)  # Should return "Toyota"
print(car.doors)  # Should return 4


# Medium - 2

class BankAccount:
    def __init__(self,account_number, balance):
        self.account_number = account_number
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
    def get_balance(self):
        return self.__balance
    def get_account_number(self):
        return self.__account_number
# Example usage:
account = BankAccount("123456", 1000)
print(account.get_balance())  # Should return 1000
account.deposit(500)
print(account.get_balance())  # Should return 1500
account.withdraw(200)
print(account.get_balance())  # Should return 1300
print(account.get_account_number())  # Should return "123456"

# Direct access should not be allowed
try:
    account._balance = 2000  # This should be discouraged or prevented
except AttributeError:
    print("Cannot directly access private attribute")
    


        
        
    