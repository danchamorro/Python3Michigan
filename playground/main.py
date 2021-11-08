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

print(spidlimbs)
print(spider.arms)

vals = [25, 30, 33, 35, 40, 180]
# do a list comprehension that that adds 32 to each value in the vals list and save the result to a variable called new_vals
new_vals = [val + 32 for val in vals]

# for val in vals:
#     new_vals.append(val + 32)

print(new_vals)

# Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false with list comprehension.


def bool_to_word(boolean):
    return "Yes" if boolean else "No"


print(bool_to_word(False))
