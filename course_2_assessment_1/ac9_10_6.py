# Challenge: Create a list called emotions that contains the first word of every line in emotion_words.txt

file_obj = open("emotion_words.txt", "r")
lines = file_obj.readlines()

emotions = []

for line in lines:
    line = line.split()
    emotions.append(line[0])

file_obj.close()

print(emotions)
