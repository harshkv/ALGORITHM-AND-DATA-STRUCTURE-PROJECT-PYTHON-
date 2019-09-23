from collections import deque, namedtuple


# initialize all nodes to infinity
inf = float('inf')
Edge = namedtuple('Edge', 'start, end, cost')


def make_edge(start, end, cost=1):
  return Edge(start, end, cost)


class Graph:
    def __init__(self, edges):
        incorrect_edges = [i for i in edges if len(i) not in [2, 3]]
        if incorrect_edges:
            raise ValueError('Wrong edges data: {}'.format(incorrect_edges))

        self.edges = [make_edge(*edge) for edge in edges]

    @property
    def vertices(self):
        return set(
            sum(
                ([edge.start, edge.end] for edge in self.edges), []
            )
        )

    def get_node_pairs(self, n1, n2, both_ends=True):
        if both_ends:
            node_pairs = [[n1, n2], [n2, n1]]
        else:
            node_pairs = [[n1, n2]]
        return node_pairs

    def remove_edge(self, n1, n2, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        edges = self.edges[:]
        for edge in edges:
            if [edge.start, edge.end] in node_pairs:
                self.edges.remove(edge)

    def add_edge(self, n1, n2, cost=1, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        for edge in self.edges:
            if [edge.start, edge.end] in node_pairs:
                return ValueError('Edge {} {} already exists'.format(n1, n2))

        self.edges.append(Edge(start=n1, end=n2, cost=cost))
        if both_ends:
            self.edges.append(Edge(start=n2, end=n1, cost=cost))

    @property
    def neighbours(self):
        neighbours = {vertex: set() for vertex in self.vertices}
        for edge in self.edges:
            neighbours[edge.start].add((edge.end, edge.cost))

        return neighbours

    def dijkstra(self, source, dest):
        global distances
        assert source in self.vertices, 'Such source node doesnt exist'
        distances = {vertex: inf for vertex in self.vertices}
        pre_node = {
            vertex: None for vertex in self.vertices
        }
        distances[source] = 0
        vertices = self.vertices.copy()

        while vertices:
            present_node = min(
                vertices, key=lambda vertex: distances[vertex])
            vertices.remove(present_node)
            if distances[present_node] == inf:
                break
            for neighbour, cost in self.neighbours[present_node]:
                other_path = distances[present_node] + int(cost)
                if other_path < distances[neighbour]:
                    distances[neighbour] = other_path
                    pre_node[neighbour] = present_node

        path, present_node = deque(), dest
        while pre_node[present_node] is not None:
            path.appendleft(present_node)
            present_node = pre_node[present_node]
        if path:
            path.appendleft(present_node)
        return path,distances

f1 = open(r'inp2.txt','r')
distances =  ()
a = []
var =[]
for i in f1.readlines():
        p=i.split()
        a.append(p)

inp =[]
length = len(a)
no_of_vertices =int( a[0][0])
no_of_edges = int(a[0][1])
directed = str(a[0][2])
graph = a[1:length-1]
for i in range(1,no_of_edges+1):
  if(a[i][0] and a[i][1] not in inp):
    inp.append(a[i][0])
    inp.append(a[i][1])
if(directed == 'D'):

  print("The number of Vertices is :",no_of_vertices)
  print("The number of Edges is :",no_of_edges, "\n")
  graph = Graph(graph)
  print ("NOTE : \nThe source node is A, we traverse to the destination node (could be any node),and then we also get the shortest path to all other nodes in the graph from A. If there is no path, it would be infinity, as it is a directed graph.")
  print("Directed Graph – Djikstra’s – Output: ")
  print("The path from the source to every other node in the directed \n")

  for q in range(1,len(inp)):
    out =graph.dijkstra("A",inp[q])
    print(out[0])
  print ("The shortest path cost from source A to every other node is:\n ")
  print(distances)
else:
  print(" This program is for directed graphs")
  exit()           

