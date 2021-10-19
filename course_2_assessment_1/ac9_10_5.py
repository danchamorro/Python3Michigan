# Challenge: Using the file school_prompt.txt, assign the third word of every line to a list called three.

file_obj = open("school_prompt.txt", "r")
lines = file_obj.readlines()

three = []

for line in lines:
    line = line.split()
    three.append(line[2])

file_obj.close()

print(three)
