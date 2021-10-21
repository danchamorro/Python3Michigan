# Create a dictionary called low_d that keeps track of all the characters in the string p and notes how many times each
# character was seen. Make sure that there are no repeats of characters as keys,
# such that “T” and “t” are both seen as a “t” for example.

p = "Summer is a great time to go outside. You have to be careful of the sun though because of the heat."

p_lower = p.lower()

low_d = {}

for char in p_lower:
    if char not in low_d:
        low_d[char] = 0
    low_d[char] += 1

print(low_d)
