import json
import collections
from pprint import pprint
data = {}

#load the json
with open("sf_json_all.json") as data_file:
    data = json.load(data_file)

n_file = open('sf_nodes_dual.txt','w')
e_file = open('sf_edges_dual.txt','w')

ways = []
intersect_hash = {}

#count the links of each node, since we need it to split ways later
for e in data["elements"]:
    if e["type"] == "way" and 'tags' in e and "highway" in e["tags"]: #it is a road
        if all (k != e["tags"]["highway"] for k in ("pedestrian","footway", "cycleway", "bridleway")): #if its not a walk or bike way
            ways.append(e)
            for n in e['nodes']:
                if e["id"] not in intersect_hash:
                    intersect_hash[e["id"]] = []
                intersect_hash[e["id"]].append(n)

for edge in intersect_hash:
    n_file.write(str(edge) + "\n")
    num_inters = len(intersect_hash[edge])
    for i in range(num_inters):
        for j in range(i, num_inters):
            if i != j:
                e_file.write(str(intersect_hash[edge][i]) + " " + str(intersect_hash[edge][j]) + "\n")
print "number of streets:", len(ways)

