# Define a class called Bike that accepts a string and a float as input, and assigns those inputs respectively to two instance variables, color and price. Assign to the variable testOne an instance of Bike whose color is blue and whose price is 89.99. Assign to the variable testTwo an instance of Bike whose color is purple and whose price is 25.0.


class Bike:
    def __init__(self, color, price):
        self.color = color
        self.price = price


testOne = Bike("blue", 89.99)
testTwo = Bike("purple", 25.00)
