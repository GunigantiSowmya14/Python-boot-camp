class Animal:
    def speak():
        return"animal speaking"
class Dog(Animal):
    def bark():
        return "bow..."
    #single inheritence
class Puppy(Dog):
    def puppy_speak():
        return "i am puppy"
obj1=Puppy
print(obj1.speak())
print(obj1.bark())
print(obj1.puppy_speak())
