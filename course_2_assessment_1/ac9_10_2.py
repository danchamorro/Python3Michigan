# We have provided a file called emotion_words.txt that contains lines of words that describe emotions.
# Find the total number of words in the file and assign this value to the variable num_words.

file_obj = open("emotion_words.txt", "r")
lines = file_obj.read().split()

num_words = 0

for word in lines:
    num_words += 1

file_obj.close()

print(num_words)
