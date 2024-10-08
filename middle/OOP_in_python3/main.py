class Car:

    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f"The {self.color} car has {self.mileage:,} miles"

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

class GoldenRetriever(Dog):

    def speak(self, sound="Bark"):
        return super().speak(sound)
    
if __name__ == "__main__":
    # car1 = Car("blue", 20_000)
    # car2 = Car("red", 30_000)

    # for car in (car1, car2):
    #     print(car)
    pass