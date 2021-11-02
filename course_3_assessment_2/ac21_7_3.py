# Below, we have provided a list of tuples that contain the names of Game of Thrones characters.
# Using list comprehension, create a list of strings called first_names that contains only the first names of everyone in the
# original list.


people = [('Snow', 'Jon'), ('Lannister', 'Cersei'), ('Stark', 'Arya'), ('Stark', 'Robb'), ('Lannister', 'Jamie'), ('Targaryen', 'Daenerys'), ('Stark',
                                                                                                                                              'Sansa'), ('Tyrell', 'Margaery'), ('Stark', 'Eddard'), ('Lannister', 'Tyrion'), ('Baratheon', 'Joffrey'), ('Bolton', 'Ramsey'), ('Baelish', 'Peter')]

first_names = [person[1] for person in people]
print(first_names)
