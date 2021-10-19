# Assign to the variable num_lines the number of lines in the file school_prompt.txt.

file_obj = open("school_prompt.txt", "r")
contents = file_obj.readlines()

num_lines = len(contents)

file_obj.close()

print(num_lines)
