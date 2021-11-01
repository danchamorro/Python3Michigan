# Below, we’ve provided a list of lists. Use in statements to create variables with Boolean values - see the ActiveCode
# window for further directions.


L = [[5, 8, 7], ['hello', 'hi', 'hola'], [6.6, 1.54, 3.99], ['small', 'large']]

# Test if 'hola' is in the list L. Save to variable name test1
test1 = bool

for elm in L:
    for word in elm:
        if type(word) is str and word == "hola":
            test1 = True
        else:
            test1 = False
print(test1)

# Test if [5, 8, 7] is in the list L. Save to variable name test2
test2 = bool

if [5, 8, 7] in L:
    test2 = True
else:
    test2 = False
print(test2)


# Test if 6.6 is in the third element of list L. Save to variable name test3
test3 = bool
fsix = 6.6


if fsix in L[2]:
    test3 = True
else:
    test3 = False
print(test3)
