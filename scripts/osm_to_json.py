import overpass
import json
from pprint import pprint

api = overpass.API()
# response = api.Get('node["name"="San Francisco"]')
# pprint(convert(response))

# map_query = overpass.MapQuery(50.746,7.154,50.748,7.157)
map_query = overpass.MapQuery(37.7,-122.53,37.82,-122.36)
response = api.Get(map_query)
print json.dumps(response)
