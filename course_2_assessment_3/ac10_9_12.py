# Create a dictionary, freq_words, that contains each word in string str1 as the key and its frequency as the value.


str1 = "I wish I wish with all my heart to fly with dragons in a land apart"

freq_words = {}

str1_lst = str1.split()

for word in str1_lst:
    if word not in freq_words:
        freq_words[word] = 0
    freq_words[word] = freq_words[word] + 1

print(freq_words)
