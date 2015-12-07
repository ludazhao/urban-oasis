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

primary_roads = []
for line in e_file:
	ids = line.rstrip().split()
	edge_ids[(int(ids[0]), int(ids[1]))] = int(ids[2])
	if ids[3] in ["primary", "secondary", "tertiary"]:
		primary_roads.append(int(ids[2]))

for line in e_data_file:
	data = line.rstrip().split(':{')
	edge_data[int(data[0])] = data[1][:-1]

for line in n_file:
	data = line.rstrip().split()
	nodes[int(data[0])] = (float(data[1]), float(data[2]))

# edge_attr = {}
# for nPair in edge_ids:
# 	edge_attr[nPair] = edge_data[edge_ids[nPair]]

G = snap.LoadEdgeList(snap.PUNGraph, 'n_sf_edges.txt', 0, 1)

G_dual = snap.LoadEdgeList(snap.PUNGraph, 'n_sf_edges_dual.txt', 0, 1)

candidates = []
low_betweenness = []
Node_betweenness_dual = snap.TIntFltH()
Edge_betweenness_dual = snap.TIntPrFltH()
snap.GetBetweennessCentr(G_dual, Node_betweenness_dual, Edge_betweenness_dual)
Node_betweenness_dual.Sort(False, True)
rank = 1
for item in Node_betweenness_dual:
	if item not in primary_roads:
		continue
	if rank > 1000:
		break
	# print "%d : %f" % (item, Node_betweenness_dual[item])
	low_betweenness.append(item)
	rank += 1
print "-----------------"

closeness_dual = snap.TIntFltH()
for n in G_dual.Nodes():
	nId = n.GetId()
	closeness_dual[nId] = snap.GetClosenessCentr(G_dual, nId)
closeness_dual.Sort(False, False)
rank = 1
for item in closeness_dual:
	if item not in primary_roads:
		continue
	if rank > 100:
		break
	# print "%d : %f" % (item, closeness_dual[item])
	if item in low_betweenness:
		candidates.append(item)
	rank += 1
print "-----------------"
print "number of candidates: %d" % len(candidates)
print candidates

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