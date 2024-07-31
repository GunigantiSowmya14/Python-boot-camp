class Animal:
    def speak():
        return "animal"
class Dog(Animal):
    def speak():
        return "bow..."
class Puppy(Dog):
    def speak():
        return "i am puppy"
obj1=Puppy
print(obj1.speak())
