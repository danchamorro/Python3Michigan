# Assign the first 33 characters from the textfile, travel_plans.txt to the variable first_chars.

file_obj = open("travel_plans.txt", "r")
contents = file_obj.read()

first_chars = ""

for char in contents[:33]:
    first_chars = first_chars + char

file_obj.close()

print(first_chars)
