# Sort the following list by each element’s second letter a to z. Do so by using lambda.
# Assign the resulting value to the variable lambda_sort.

ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']

lambda_sort = sorted(ex_lst, key=lambda x: x[1])

print(lambda_sort)
