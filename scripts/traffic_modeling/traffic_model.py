import snap
import math
from geopy.distance import vincenty

#Elena did this
#def getDistance(coor1, coor2):
#    return math.sqrt(pow(coor1[0] - coor2[0], 2) + pow(coor1[1] - coor2[1], 2))


#Class for traffic model.
class TrafficModel:

    # graph: snappy graph, node_attr: a dict of n1 to node coordinates(lat, long), edge_typo, edge_speed: a dict of (n1, n2) to edge properties, n_to_e: a link from (n1, n2) to a list of edge ids(to preserve which edges are part of the same road)
    # the only changing variables to calculate our trafficmodel is self.e_flow and self.e_time. All other variables are constant
    def __init__(self, graph, node_attr, edge_typo, edge_speed, n_to_e):
        self.graph = graph
        self.node_coor = node_attr #the coordinate of each node
        self.e_type = edge_typo #the typology of each edge
        self.e_dist = {} #the distance for each edge
        self.e_speed = edge_speed # the maximum allowed speed of each edge.

        #get maximum speed for all edge
        #residential: 15
        for e in self.e_speed:
            e_type = self.e_type[e]
            if self.e_speed[e] == 'N/A':
                if e_type == 'residential':
                    self.e_speed[e] = 20
                elif e_type == 'tertiary':
                    self.e_speed[e] = 25
                elif e_type == 'secondary':
                    self.e_speed[e] = 25
                elif e_type == 'primary':
                    self.e_speed[e] = 35
                elif e_type == 'motorway':
                    self.e_speed[e] = 55
                else:
                    self.e_speed[e] = 25
            else:
              speed = int(self.e_speed[e])

        #calculate distance for each edge(loop over e_type since it contains all edges)
        for e in self.e_type:
            coor1 = self.node_coor[e[0]]
            coor2 = self.node_coor[e[1]]

            dist2 = vincenty(coor1, coor2).miles
            self.e_dist[(int(e[0]), int(e[1]))] = dist2

        #initializae the # of cars to be 0 on all edges
        self.e_flow = {}
        for e in self.e_type:
            self.e_flow[(int(e[0]), int(e[1]))] = 0

        self.e_time = {} #the time needed to traverse an edge. Used as the weight in our Dijkstras
        for e in self.e_time:
            self.e_time[e] = self.e_dist[e] * 60 / float(self.e_speed[e]) # in minutes

        print self.e_time
