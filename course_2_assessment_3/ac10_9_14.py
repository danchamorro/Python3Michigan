# Create the dictionary characters that shows each character from the string sally and its frequency.
# Then, find the most frequent letter based on the dictionary. Assign this letter to the variable best_char.

sally = "sally sells sea shells by the sea shore"

characters = {}

for char in sally:
    if char not in characters:
        characters[char] = 0
    characters[char] = characters[char] + 1

# print(characters)

ks = characters.keys()
best_char = list(ks)[0]

for key in ks:
    if characters[key] > characters[best_char]:
        best_char = key

print(best_char)
