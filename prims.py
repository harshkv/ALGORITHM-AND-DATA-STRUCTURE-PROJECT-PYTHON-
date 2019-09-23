from collections import defaultdict
from heapq import *
 
def prims( nodes, edges ):
    curr = defaultdict( list )
    for v1,v2,c in edges:
        curr[ v1 ].append( (c, v1, v2) )
        curr[ v2 ].append( (c, v2, v1) )
 
    mst = []
    used = set( nodes[ 0 ] )
    available_edges = curr[ nodes[0] ][:]
    heapify( available_edges )
 
    while available_edges:
        cost, v1, v2 = heappop( available_edges )
        if v2 not in used:
            used.add( v2 )
            mst.append( ( v1, v2, cost ) )
 
            for q in curr[ v2 ]:
                if q[ 2 ] not in used:
                    heappush( available_edges, q )
    return mst
 
#test
nodes =[]
varlist = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
varlist =list(varlist)
f1 = open(r'inp2_undirected.txt','r')

a = []

for i in f1.readlines():
        p=i.split()
        a.append(p)
cost = 0
length = len(a)
no_of_vertices =int(a[0][0])
no_of_edges = int(a[0][1])
undirected = str(a[0][2])
edges = a[1:length-1]
if(undirected == 'U'):
  print("The minimum spanning tree using Prim's Algorithm")
  print("The number of Vertices is :", no_of_vertices)
  print("The number of Edges is :", no_of_edges)
  for i in range(0,no_of_vertices):
      nodes.append(varlist[i])
  out = prims( nodes, edges )
  j= 0 
  for i in out:
      print (i)
      cost += int(out[j][2])
      j +=1 
  print("Total cost =" ,cost)


