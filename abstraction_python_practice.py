class Animal:
    def __init__(self):
        pass
class Dog(Animal):
    def sound(self):
        print("barking")
class Cat(Animal):
    def sound(self):
        print("meowing")
d=Dog()
d.sound()
c=Cat()
c.sound()

#NEWFILE
from abc import ABC,abstractmethod
import abstraction_python_practice
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass





class FoodDeliveryApp:
    def deliver(self):
        pass
class Zomato(FoodDeliveryApp):
    def deliver(self):
        print("delivered by Zomato")
class Swiggy(FoodDeliveryApp):
    def deliver(Self):
        print("delivered by Swiggy")
z=Zomato()
z.deliver()
s=Swiggy()
s.deliver()

#NEWFILE
from abc import ABC,abstractmethod
import abstraction_python_practice
class FoodDeliveryApp(ABC):
    @abstractmethod
    def deliver(self):
        pass
