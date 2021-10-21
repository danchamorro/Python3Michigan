# Find the least frequent letter. Create the dictionary characters that shows each character from string sally and its frequency.
# Then, find the least frequent letter in the string and assign the letter to the variable worst_char.

sally = "sally sells sea shells by the sea shore"

characters = {}

for char in sally:
    if char not in characters:
        characters[char] = 0
    characters[char] = characters[char] + 1

# print(characters)

ks = characters.keys()
worst_char = list(ks)[0]

for key in ks:
    if characters[key] < characters[worst_char]:
        worst_char = key

print(worst_char)
