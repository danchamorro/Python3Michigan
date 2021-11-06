
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_movies_from_tastedive("Bridesmaids")
# get_movies_from_tastedive("Black Panther")

def get_movies_from_tastedive(movie_name):
    import requests_with_caching
    import json
    baseurl = 'https://tastedive.com/api/similar'
    params_d = {}
    params_d['q'] = movie_name
    params_d['type'] = 'movies'
    params_d['limit'] = 5
    resp = requests_with_caching.get(baseurl, params=params_d)
    data = resp.json()
    return data


# Next, you will need to write a function that extracts just the list of movie titles from a dictionary returned by get_movies_from_tastedive. Call it extract_movie_titles.
def extract_movie_titles(dic):
    movie_titles = []
    for movie in dic['Similar']['Results']:
        movie_titles.append(movie['Name'])
    return movie_titles


# Next, you’ll write a function, called get_related_titles. It takes a list of movie titles as input. It gets five related movies for each from TasteDive, extracts the titles for all of them, and combines them all into a single list. Don’t include the same movie twice.
def get_related_titles(movie_list):
    related_titles = []
    for movie in movie_list:
        related_titles.extend(extract_movie_titles(
            get_movies_from_tastedive(movie)))
    return list(set(related_titles))
