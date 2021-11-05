# Define a function that connects to datamuse.com and returns a list of words that rhyme with the input string.
def get_rhymes(word):
    import requests
    import json
    import re
    url = 'https://api.datamuse.com/words'
    params = {'ml': word}
    response = requests.get(url, params=params)
    data = response.json()
    for words in data:
        return(words['word'])


print(get_rhymes("ringing in the ears"))
