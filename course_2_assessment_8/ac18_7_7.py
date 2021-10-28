# Sort the list ids by the last four digits of each id. Do this using lambda and not using a defined function.
# Save this sorted list in the variable sorted_id.


ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]

sorted_id = sorted(ids, key=lambda x: str(x)[-4:])

print(sorted_id)
