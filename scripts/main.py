import snap

e_file = open("n_sf_edges.txt", 'r')
e_data_file = open("n_sf_edges_data.txt", 'r')
n_file = open("n_sf_nodes.txt", 'r')
# maps from the pair of source and destination nodes to the edge id
# ex. (33242031 65292114) -> 5004035
edge_ids = {}
edge_data = {}
# maps from the node idea to its coordinates
nodes = {}

for line in e_file:
	ids = line.rstrip().split()
	edge_ids[(int(ids[0]), int(ids[1]))] = int(ids[2])

for line in e_data_file:
	data = line.rstrip().split(':{')
	edge_data[int(data[0])] = data[1][:-1]

for line in n_file:
	data = line.rstrip().split()
	nodes[int(data[0])] = (float(data[1]), float(data[2]))

G = snap.LoadEdgeList(snap.PUNGraph, 'n_sf_edges.txt', 0, 1)
print G.GetNodes()
print G.GetEdges()

G_dual = snap.LoadEdgeList(snap.PUNGraph, 'n_sf_edges_dual.txt', 0, 1)
print G_dual.GetNodes()
print G_dual.GetEdges()

# testing code
# for n in G.Nodes():
# 	coords = nodes[n.GetId()]

# for edge in G.Edges():
# 	src = edge.GetSrcNId()
# 	dest = edge.GetDstNId()
# 	if (src, dest) in edge_ids:
# 		data = edge_data[edge_ids[(src, dest)]]
# 	else:
# 		data = edge_data[edge_ids[(dest, src)]]