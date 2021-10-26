# The following function, greeting, does not work. Please fix the code so that it runs without error.
# This only requires one change in the definition of the function.

def greeting(name, greeting="Hello ", excl="!"):
    return greeting + name + excl


print(greeting("Bob"))
print(greeting(""))
print(greeting("Bob", excl="!!!"))
