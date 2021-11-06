
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


# Your next task will be to fetch data from OMDB. The documentation for the API is at https://www.omdbapi.com/

# Define a function called get_movie_data. It takes in one parameter which is a string that should represent the title of a movie you want to search. The function should return a dictionary with information about that movie.

# Again, use requests_with_caching.get(). For the queries on movies that are already in the cache, you won’t need an api key. You will need to provide the following keys: t and r. As with the TasteDive cache, be sure to only include those two parameters in order to extract existing data from the cache.
def get_movie_data(movie_title):
    import requests_with_caching
    import json
    baseurl = 'http://www.omdbapi.com/'
    params_d = {}
    params_d['t'] = movie_title
    params_d['r'] = 'json'
    resp = requests_with_caching.get(baseurl, params=params_d)
    data = json.loads(resp.text)
    return data


# Now write a function called get_movie_rating. It takes an OMDB dictionary result for one movie and extracts the Rotten Tomatoes rating as an integer. For example, if given the OMDB dictionary for “Black Panther”, it would return 97. If there is no Rotten Tomatoes rating, return 0.
def get_movie_rating(movie_dic):
    if 'Ratings' in movie_dic:
        for rating in movie_dic['Ratings']:
            if rating['Source'] == 'Rotten Tomatoes':
                return int(rating['Value'][:-1])
    return 0


# Define a function get_sorted_recommendations. It takes a list of movie titles as an input. It returns a sorted list of related movie titles as output, up to five related movies for each input movie title. The movies should be sorted in descending order by their Rotten Tomatoes rating, as returned by the get_movie_rating function. Break ties in reverse alphabetic order, so that ‘Yahşi Batı’ comes before ‘Eyyvah Eyvah’.
def get_sorted_recommendations(movie_list):
    related_titles = get_related_titles(movie_list)
    movie_ratings = []
    for movie in related_titles:
        movie_ratings.append((get_movie_rating(
            get_movie_data(movie)), movie))
    movie_ratings.sort(reverse=True)
    return [movie[1] for movie in movie_ratings]
