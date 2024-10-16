class Vehicle:
    def __init__(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def toString(self):
        return f"This vehicle is {self.color}"

class Car(Vehicle):
    def __init__(self, color, winter_tires=False):
        super().__init__(color)  
        self.winter_tires = winter_tires  # New instance variable for winter tires

    def toString(self):
        # Using the Vehicle's toString method and adding winter tires info
        base_string = super().toString()
        return f"{base_string}\nHas winter tires: {self.winter_tires}"

