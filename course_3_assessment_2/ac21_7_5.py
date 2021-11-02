# Below, we have provided a list of tuples that contain students’ names and their final grades in PYTHON 101.
# Using list comprehension, create a new list passed that contains the names of students who passed the class
# (had a final grade of 70 or greater).

students = [('Tommy', 95), ('Linda', 63), ('Carl', 70),
            ('Bob', 100), ('Raymond', 50), ('Sue', 75)]

passed = [student[0] for student in students if student[1] >= 70]

print(passed)
