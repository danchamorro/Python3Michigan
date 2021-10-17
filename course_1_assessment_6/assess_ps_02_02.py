# Write one for loop to print out each element of the list several_things. Then, write another for loop to print out the
# TYPE of each element of the list several_things. To complete this problem you should have written two different for loops,
# each of which iterates over the list several_things, but each of those 2 for loops should have a different result.

several_things = ["hello", 2, 4, 6.0, 7.5, 234352354, "the end", "", 99]

for i in several_things:
    print(i)

for i in several_things:
    print(type(i))
