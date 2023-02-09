import sys
import heapq as hq

def read_in_network(DATA):
    
    with open(DATA, 'r') as f:
    
        header = f.readline()
        num_nodes = int(header.split()[0])
        
        network = [[] for k in range(num_nodes+1)] 
        
        for line in f :
            line = line.split()
            if len(line) == 3:       
                #edges stored as (weight, source, destination)
                network[int(line[0])].append((int(line[2]), int(line[0]), int(line[1])))
                network[int(line[1])].append((int(line[2]), int(line[1]), int(line[0])))
    return network
        
def pick_min(list):
    heap = []
    
    for k in range(len(list)):
        hq.heappush(heap, (list[k][0], k))
    
    _, index = hq.heappop(heap)
    
    return index

def prims_MST(network):

    tree = [[] for k in range(len(network)+1)]
    span = 0
    visited = [False for k in range(len(network)+1)]
    heap = []
    
    source = 1
    while len(network[source]) < 1 : source += 1
    
    for edge in network[source]:
        hq.heappush(heap, edge)
    
    visited[source] = True
    
    while heap :
        weight, source, dest = hq.heappop(heap)
        
        if visited[dest] == True:
            continue
        
        visited[dest] = True
        tree[source].append((weight, dest))
        span += weight
        
        for neighb in network[dest]:
            _, _, n_dest = neighb
            
            if visited[n_dest] == False:
                hq.heappush(heap, neighb)
   
    return span, tree
    

DATA = sys.argv[1]
network = read_in_network(DATA)

span, tree = prims_MST(network)

print("span is : \n", span)
