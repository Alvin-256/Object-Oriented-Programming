class Customer:
    def __init__(self, name, address):
        self.name = name  # Instance variable for the customer's name
        self.address = address  # Instance variable for the customer's address

    def getName(self):
        return self.name  # Method to retrieve the customer's name

    def getAddress(self):
        return self.address  # Method to retrieve the customer's address

    def toString(self):
        return f"Customer Name: {self.name}, Address: {self.address}"  # Method to represent the customer as a string

