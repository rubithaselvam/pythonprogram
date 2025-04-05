class Bird:
    def __init__(self, name): # constructor key word __init__
        self.name = name

    def fly(self):
        print(f"{self.name} can fly!")

class Sparrow(Bird):
    def kuku(self):
        print(f"{self.name} says heyyyyyy!")

class BabySparrow(Sparrow):
    def learn_to_fly(self):
        print(f"{self.name} is learning to fly!")


baby = BabySparrow("SPARROW")
baby.fly()
baby.kuku()
baby.learn_to_fly()
