# Create a dictionary, freq, that displays each character in string str1 as the key and its frequency as the value.

str1 = "peter piper picked a peck of pickled peppers"

freq = {}

for letter in str1:
    if letter not in freq:
        freq[letter] = 0
    freq[letter] = freq[letter] + 1

print(freq)
