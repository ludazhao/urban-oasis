import snap
from traffic_model import TrafficModel

e_file = open("../n_sf_edges.txt", 'r')
n_file = open("../n_sf_nodes.txt", 'r')
# maps from the pair of source and destination nodes to typology and speed
# ex. (33242031 65292114) -> "primary"
# ex. (33242031 65292114) -> "25"(or "N/A")
edge_typo = {}
edge_speed = {}
edge_lanes = {}
nd_to_e = {}
# maps from the node idea to its coordinates
nodes = {}
graph = {}

for line in e_file:
    ids = line.rstrip().split()
    if ids[0] == ids[1]:
        continue
    if (int(ids[0]), int(ids[1])) == (14282, 10113):
        continue
    e1 = int(ids[0])
    e2 = int(ids[1])
    if e1 not in graph:
        graph[e1] = []
    if e2 not in graph:
        graph[e2] = []

    graph[e1].append(e2)
    if ids[6] == "no":
        graph[e2].append(e1)
        edge_typo[(int(ids[1]), int(ids[0]))] = ids[3]
        edge_speed[(int(ids[1]), int(ids[0]))] = ids[4]
        edge_lanes[(int(ids[1]), int(ids[0]))] = ids[5]
        nd_to_e[(int(ids[1]), int(ids[0]))] = ids[2]

    edge_typo[(int(ids[0]), int(ids[1]))] = ids[3]
    edge_speed[(int(ids[0]), int(ids[1]))] = ids[4]
    edge_lanes[(int(ids[0]), int(ids[1]))] = ids[5]
    nd_to_e[(int(ids[0]), int(ids[1]))] = ids[2]

for line in n_file:
    data = line.rstrip().split()
    nodes[int(data[0])] = (float(data[1]), float(data[2]))

G = snap.LoadEdgeList(snap.PUNGraph, '../n_sf_edges.txt', 0, 1)
model = TrafficModel(G,graph, nodes, edge_typo, edge_speed, edge_lanes, nd_to_e)
model.iterate(20, 100)

#candidates = [7863, 9460, 7702, 8781, 3716, 345, 3717, 3263, 4469, 4470, 7698, 4658, 8743]
#for e in nd_to_e:
#    if nd_to_e[e] in candidates:
#        graph[e[0]].remove(e[1])

# model = TrafficModel(G, graph, nodes, edge_typo, edge_speed, edge_lanes, nd_to_e)
# model.iterate(10, 1000)
