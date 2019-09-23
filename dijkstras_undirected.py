from collections import defaultdict
from heapq import *

def dijkstra(edges, f, t):
    g = defaultdict(list)
    for l,r,c in edges:
        g[l].append((c,r))

    q, seen, mins = [(0,f,())], set(), {f: 0}
    while q:
        (cost,v1,path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            print(path,cost)
            if v1 == t: return (cost, path)

            for c, v2 in g.get(v1, ()):
                if v2 in seen: continue
                prev = mins.get(v2, None)
                next = cost + int(c)
                if prev is None or next < prev:
                    mins[v2] = next
                    heappush(q, (next, v2, path))

    return (dijkstra(edges,t,f))

f1 = open(r'inp2_undirected2.txt','r')
a = []
for i in f1.readlines():
        p=i.split()
        a.append(p)
 
inp = []
length = len(a)
no_of_vertices =int( a[0][0])
no_of_edges = int(a[0][1])
undirected = str(a[0][2])
for i in range(1,no_of_edges+1):
  if(a[i][0] and a[i][1] not in inp):
    inp.append(a[i][0])
    inp.append(a[i][1])

edges = a[1:length-1]
if(undirected == 'U'):
  print ("=== Dijkstra for undirected  ===")
  print ("NOTE : \n The source node is A, we traverse to the destination node (could be any node). Since, this is an undirected graph, the source to destination as well as reverse would have the same shortest path and we could traverse bothways. We print them according to all the subpaths and costs.")
  print("The number of Vertices is :",no_of_vertices)
  print("The number of Edges is :",no_of_edges)
  for q in range(1,len(inp)):
      out = dijkstra(edges, "A", inp[q])
      print("The path traversal from source A to", inp[q])
      print(out[0])
  print(out)

