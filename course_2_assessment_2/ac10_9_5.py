# Create a list of the countries that are in the dictionary golds, and assign that list to the variable name countries.
# Do not hard code this.


golds = {"Italy": 12, "USA": 33, "Brazil": 15, "China": 27,
         "Spain": 19, "Canada": 22, "Argentina": 8, "England": 29}

countries = []

for key in golds:
    countries.append(key)

print(countries)
