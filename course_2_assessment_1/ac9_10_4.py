# Assign the first 30 characters of school_prompt.txt as a string to the variable beginning_chars.

file_obj = open("school_prompt.txt", "r")
contents = file_obj.read()

beginning_chars = ""

for char in contents[:30]:
    beginning_chars = beginning_chars + char

file_obj.close()

print(beginning_chars)
