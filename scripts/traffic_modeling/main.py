import snap
from traffic_model import TrafficModel

e_file = open("../n_sf_edges.txt", 'r')
n_file = open("../n_sf_nodes.txt", 'r')
# maps from the pair of source and destination nodes to typology and speed
# ex. (33242031 65292114) -> "primary"
# ex. (33242031 65292114) -> "25"(or "N/A")
edge_typo = {}
edge_speed = {}
nd_to_e = {}
# maps from the node idea to its coordinates
nodes = {}

for line in e_file:
	ids = line.rstrip().split()
	edge_typo[(int(ids[0]), int(ids[1]))] = ids[3]
	edge_speed[(int(ids[0]), int(ids[1]))] = ids[4]
	nd_to_e[(int(ids[0]), int(ids[1]))] = ids[2]

for line in n_file:
	data = line.rstrip().split()
	nodes[int(data[0])] = (float(data[1]), float(data[2]))

G = snap.LoadEdgeList(snap.PUNGraph, '../n_sf_edges.txt', 0, 1)

TrafficModel(G, nodes, edge_typo, edge_speed, nd_to_e)



