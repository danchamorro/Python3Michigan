# Challenge: Using the file school_prompt.txt, if the character ‘p’ is in a word, then add the word to a list called p_words.

file_obj = open("school_prompt.txt", "r")
lines = file_obj.readlines()

p_words = []

for word in lines:
    word = word.split()
    for char in word:
        if "p" in char:
            p_words.append(char)

file_obj.close()

print(p_words)
