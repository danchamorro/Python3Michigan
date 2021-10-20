# Provided is a string saved to the variable name s1. Create a dictionary named counts that contains each
# letter in s1 and the number of times it occurs.

s1 = "hello"

counts = {}

for letter in s1:
    if letter not in counts:
        counts[letter] = 0
    counts[letter] = counts[letter] + 1

print(counts)
