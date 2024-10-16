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
        self.winter_tires = winter_tires

    def toString(self):
        base_string = super().toString()
        return f"{base_string}\nHas winter tires: {self.winter_tires}"

class Truck(Vehicle):
    def __init__(self, color, trailer=False):
        super().__init__(color)
        self.trailer = trailer

    def toString(self):
        base_string = super().toString()
        return f"{base_string}\nHas trailer: {self.trailer}"

class Garage:
    def __init__(self):
        self.parked_vehicle = None  # Initializing with no vehicle parked

    def setVehicle(self, vehicle):
        self.parked_vehicle = vehicle  
    def toString(self):
        if self.parked_vehicle:
            return f"Description of the parked vehicle:\n{self.parked_vehicle.toString()}"
        else:
            return "No vehicle is parked in the garage."


