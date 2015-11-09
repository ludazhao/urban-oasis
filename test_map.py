import overpass
from pprint import pprint

# converts from unicode to ASCII encoding
def convert(input):
    if isinstance(input, dict):
        return {convert(key): convert(value) for key, value in input.iteritems()}
    elif isinstance(input, list):
        return [convert(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input

api = overpass.API()
# response = api.Get('node["name"="San Francisco"]')
# pprint(convert(response))

# map_query = overpass.MapQuery(50.746,7.154,50.748,7.157)
map_query = overpass.MapQuery(37.7,-122.53,37.82,-122.36)
response = api.Get(map_query)
pprint(convert(response))