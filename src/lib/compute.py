#Example of file "compute" which created using Python language programming.


# Exercise 1: Viewing and Establishing the Status of a File


class Compute:
    def __init__(self, operator, operands):
        self.operator = operator
        self.operands = operands


    def add(self):
        pass


    def subtract(self):
        pass


    def divide(self):
        pass


    def multiply(self):
        pass


# Exercise 2: Examining Differences Between Files

    def multiply(self):
        if self.operands is None:
            return
        product = 1
        for item in self.operands:
        product *= item
    print(product)

    
# Exercise 3: Adding Files to the Index

    def subtract(self):
        difference = 0
        for item in self.operands:
        difference -= item
    print(difference)


# Exercise 1: Feature-Branch Work ow-Driven Delivery

    def exponent(self):
        num_exponent = self.operands[0] ** self.operands[1]
    print(num_exponent)


