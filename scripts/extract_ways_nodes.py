import json
import collections
from pprint import pprint
data = {}

#load the json
with open("sf_json_all.json") as data_file:
    data = json.load(data_file)

n_file = open('sf_nodes.txt','w')
e_file = open('sf_edges.txt','w')
e_data_file = open('sf_edges_data.txt', 'w')

ways = []
nodes_link = collections.Counter()

#count the links of each node, since we need it to split ways later
for e in data["elements"]:
    if e["type"] == "way" and 'tags' in e and "highway" in e["tags"]: #it is a road
        if all (k != e["tags"]["highway"] for k in ("pedestrian","footway", "cycleway", "bridleway")): #if its not a walk or bike way
            ways.append(e)
            for n in e['nodes']:
                nodes_link[n]+=1

print "number of streets:", len(ways)

nodes_list = set()
#loop over it a second time to find intersections
count = 0
for e in ways:
    if len(e['nodes']) == 0:
        print e
        print "error: a way have no nodes"
        exit()
    start = e['nodes'][0]
    end = e['nodes'][-1]
    if (start == end):
        print "THis freaking way only have 1 node"
        count+=1
        continue

    # if there are intersections, break the road into multiple edges
    for i in range(len(e['nodes'])):
        if i != 0 and i != len(e['nodes']) - 1:
            n = e['nodes'][i]
            if nodes_link[n] > 1:

                end = n

                output = []
                output.append(str(start))
                output.append(str(end))
                nodes_list.add(start)
                nodes_list.add(end)
                output.append(str(e['id']))
                output.append(str(e['tags']['highway']))
                if ('maxspeed' in e['tags']):
                    #print e['tags']['maxspeed']
                    output.append(e['tags']['maxspeed'])
                else:
                    output.append('N/A')
                e_file.write('\t'.join(output) + '\n')
                start = end

    end = e['nodes'][-1]
    if (start == end):
        print "THis sucks"
        count+=1
        continue
    output = []
    output.append(str(start))
    output.append(str(end))
    nodes_list.add(start)
    nodes_list.add(end)
    output.append(str(e['id']))
    output.append(str(e['tags']['highway']))
    if ('maxspeed' in e['tags']):
        #print e['tags']['maxspeed']
        output.append(e['tags']['maxspeed'])
    else:
        output.append('N/A')
    e_file.write('\t'.join(output) + '\n')
    e_data_file.write(str(e['id']) + ":" + json.dumps(e['tags']) + '\n')

print count

for e in data["elements"]:
    if e["type"] == "node" and e["id"] in nodes_list:
        entry = []
        entry.append(str(e['id']))
        entry.append(str(e['lat']))
        entry.append(str(e['lon']))
        n_file.write(' '.join(entry) + '\n')


