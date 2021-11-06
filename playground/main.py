# Connect to itunes api
def connect_to_itunes(artist):
    import requests
    import json
    url = 'https://itunes.apple.com/search'  # url to search
    params = {'term': artist, 'media': 'music',
              'entity': 'album', 'limit': '1'}  # parameters to search
    r = requests.get(url, params=params)  # request
    data = r.json()  # convert to json
    return json.dumps(data, indent=2)  # pretty print


# print(connect_to_itunes('taylor swift'))

# Connect to flikr api
def connect_to_flikr(keyword):
    import requests
    import json
    url = 'https://api.flickr.com/services/rest'  # url to search
    params = {'method': 'flickr.photos.search', 'api_key': '2f5ac274ecfac5a455f38745704ad084',
              'text': keyword, 'format': 'json', 'nojsoncallback': '1', 'extras': 'url_m'}  # parameters to search
    r = requests.get(url, params=params)  # request
    data = r.json()  # convert to json
    return json.dumps(data, indent=2)  # pretty print


print(connect_to_flikr('taylor swift'))
