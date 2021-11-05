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


print(connect_to_itunes('taylor swift'))
