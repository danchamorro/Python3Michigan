# The textfile, travel_plans.txt, contains the summer travel plans for someone with some commentary. Find the total number of characters in the file and save to the
# variable num.

file_obj = open("travel_plans.txt", "r")
contents = file_obj.read()

num = len(contents)

file_obj.close()

print(num)
