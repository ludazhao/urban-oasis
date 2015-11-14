

n_file = open('sf_nodes.txt','r')
e_file = open('sf_edges.txt','r')
e_data_file = open('sf_edges_data.txt', 'r')
n_dual_file = open('sf_nodes_dual.txt', 'r')
e_dual_file = open('sf_edges_dual.txt','r')

n_file_w = open('n_sf_nodes.txt','w')
e_file_w = open('n_sf_edges.txt','w')
e_data_file_w = open('n_sf_edges_data.txt', 'w')
n_dual_file_w = open('n_sf_nodes_dual.txt', 'w')
e_dual_file_w = open('n_sf_edges_dual.txt','w')

n_hash = {}
e_hash = {}

count = 0
for l in n_file:
    node_id = l.split()[0]
    if node_id not in n_hash:
        n_hash[node_id] = str(count)
        n_file_w.write(l.replace(node_id, str(count)))
        count+=1

print "node count:", count

count = 0
missing_nodes = []
for l in e_file:
    node_id = l.split()[0]
    if node_id not in n_hash:
        count+=1
        missing_nodes.append(node_id)

    node_id = l.split()[1]
    if node_id not in n_hash:
        count+=1
        missing_nodes.append(node_id)

print "extra node count(from edge list):", count

count = 0

for l in n_dual_file:
    edge_id = l.split()[0]
    if edge_id not in e_hash:
        e_hash[edge_id] = str(count)
        n_dual_file_w.write(l.replace(edge_id, str(count)))
        count+=1

count = 0
missing_edges = []
for l in e_dual_file:
    node_id = l.split()[0]
    print node_id
    if node_id not in e_hash:
        count+=1
        missing_edges.append(node_id)

    node_id = l.split()[1]
    if node_id not in e_hash:
        count+=1
        missing_edges.append(node_id)

print "extra edge count(from edge list):", count

for l in e_file:
    arr = l.split()
    if arr[0] in missing_nodes or arr[1] in missing_nodes:
        continue
    e_file_w.write(' '.join([n_hash[arr[0]], n_hash[arr[1]], e_hash[arr[2]]]) + '\n')

for l in e_dual_file:
    arr = l.split()
    if arr[0] in missing_edges or arr[1] in missing_edges:
        continue
    e_dual_file_w.write(' '.join([e_hash[arr[0]], e_hash[arr[1]]]) + '\n')

for l in e_data_file:
    arr = l.split(':')
    if arr[0] in missing_edges:
        continue
    e_data_file_w.write(l.replace(arr[0], e_hash[arr[0]]))



