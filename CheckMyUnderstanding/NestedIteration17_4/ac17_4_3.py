# Below, we have provided a list of lists named L.
# Use nested iteration to save every string containing “b” into a new list named b_strings.


L = [['apples', 'bananas', 'oranges', 'blueberries', 'lemons'], ['carrots', 'peas',
                                                                 'cucumbers', 'green beans'], ['root beer', 'smoothies', 'cranberry juice']]

b_strings = []

for lst in L:
    for word in lst:
        if "b" in word:
            b_strings.append(word)

print(b_strings)
