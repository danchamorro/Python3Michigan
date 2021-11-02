# Use list comprehension to create a list called lst2 that doubles each element in the list, lst.

lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]

lst2 = [elm * 2 for elm in lst]

print(lst2)
