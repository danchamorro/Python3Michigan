# Below, we have provided a list of strings called countries.
# Use filter to produce a list called b_countries that only contains the strings from countries that begin with B.


countries = ['Canada', 'Mexico', 'Brazil', 'Chile', 'Denmark', 'Botswana', 'Spain', 'Britain', 'Portugal', 'Russia', 'Thailand',
             'Bangladesh', 'Nigeria', 'Argentina', 'Belarus', 'Laos', 'Australia', 'Panama', 'Egypt', 'Morocco', 'Switzerland', 'Belgium']

b_countries = list(filter(lambda word: "B" in word[0], countries))

print(b_countries)
