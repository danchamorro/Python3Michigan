# The variable nested_d contains a nested dictionary with the gold medal counts for the top four countries in the past three Olympics.
# Assign the value of Great Britain’s gold medal count from the London Olympics to the variable london_gold. Use indexing.
# Do not hardcode.

nested_d = {'Beijing': {'China': 51, 'USA': 36, 'Russia': 22, 'Great Britain': 19}, 'London': {
    'USA': 46, 'China': 38, 'Great Britain': 29, 'Russia': 22}, 'Rio': {'USA': 35, 'Great Britain': 22, 'China': 20, 'Germany': 13}}

london_gold = nested_d['London']["Great Britain"]

print(london_gold)
