from collections import defaultdict
from collections import deque


def loadGraph(edgeFilename):
    f_l = defaultdict(list)
    with open(edgeFilename, 'r') as file:
        for x in file:
            l,v = map(int, x.split())
            f_l[l].append(v)
            f_l[v].append(l)
    return dict(f_l)


class MyQueue:
    def __init__(self):
        self.queue = []
    def enqueu(self,value):
        self.queue.append(value)
    def dequeue(self):
        if not self.empty():
            return self.queue.pop(0)
        else:
            return None
    def empty(self):
        return len(self.queue) ==0
    def __str__(self):
        return str(self.queue)
    
def BFS(G,s):
    dist = {vert: -1 for vert in G}
    dist[s] = 0
    checked = set([s])
    queue = deque([s])
    
    while queue:
        l = queue.popleft()
        for x in G[l]:
            if x not in  checked:
                checked.add(x)
                dist[x] = dist[l] + 1
                queue.append(x)
    return dist




def distanceDistribution(G):
    distr = defaultdict(int)
    total_dist = 0 

    for s in G.keys():
        dist = BFS(G,s)
        for d in dist.values():
            if d > 0 :
                distr[d] += 1
                total_dist += 1
    for d in distr:
        distr[d] = (distr[d]/total_dist)*100
    return dict(distr)

if __name__ =="__main__":
    G = loadGraph("edges.txt")
    distr = distanceDistribution(G)
    print(distr)


#THe distribution implies that the small world phenomena may be accurate 
# as the distance between most nodes is relatively small. 