import requests

"""
For more information on the What3Words APIs see
https://developer.what3words.com/public-api/docs

For more information of the Python Requests library see
https://docs.python-requests.org/en/latest/


To find a location on a map try this
https://what3words.com/pretty.resort.quick
"""

__apikey = 'KEY_HERE'

def w3w_from_coords(coords):
    uri = 'https://api.what3words.com/v3/convert-to-3wa'
    query = {'coordinates': coords, 'key': __apikey} 
    r = requests.get(uri, params=query)
    if r:
        return r.json()['words']
    else:
        return None


def w3w_to_coords(words):
    uri = 'https://api.what3words.com/v3/convert-to-coordinates'
    query= {'words' : words, 'key': __apikey}
    r = requests.get(uri, params=query)
    if r:
        return r.json()['coordinates']
    else:
        return None

if __name__ == "__main__": # pragma no cover
   
    coords = '50.737508,-3.532954'
    print(coords)
    words = w3w_from_coords(coords)
    print(words)
    new_coords = w3w_to_coords(words)
    print(new_coords)
