from string import ascii_uppercase
from ..algorithms.Dijkstra import shortest_path

M = [  [0 ,25, 20 ,10 ,105],
        [20 ,0 ,15, 80 ,80],
        [30, 15 ,0, 70 ,90],
        [10 ,10 ,50 ,0 ,100],
        [40 ,50, 5 ,10 ,0]]


headers = ascii_uppercase[:len(M)]
test = [dict(zip(headers,M[i])) for i in range(len(M))]
g = {headers[x]:test[x] for x in range(len(headers)) }
for k,v in g.items():
    v.pop(k)



print(shortest_path(g,"A","E"))