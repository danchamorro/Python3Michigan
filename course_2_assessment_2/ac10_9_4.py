# The dictionary golds contains information about how many gold medals each country won in the 2016 Olympics.
# But today, Spain won 2 more gold medals. Update golds to reflect this information.


golds = {"Italy": 12, "USA": 33, "Brazil": 15, "China": 27,
         "Spain": 19, "Canada": 22, "Argentina": 8, "England": 29}

golds["Spain"] = golds["Spain"] + 2

print(golds)
