# Create a class called NumberSet that accepts 2 integers as input, and defines two instance variables: num1 and num2, which hold each of the input integers. Then, create an instance of NumberSet where its num1 is 6 and its num2 is 10. Save this instance to a variable t.
class NumberSet:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2


t = NumberSet(6, 10)


class Animal:
    def __init__(self, arms, legs):
        self.arms = arms
        self.legs = legs

    def limbs(self):
        return self.arms + self.legs


spider = Animal(4, 4)

spidlimbs = spider.limbs()
