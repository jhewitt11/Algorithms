import sys
import heapq as hq

# input : TEXT FILE
# Format : assume format follows structure of data provided in C2W2 assignment
def read_in_network(DATA):
    
    network = []   
    
    with open(DATA, 'r') as f:

        for line in f:
            adj_l = []
            line = line.split()
    
            for k, val in enumerate(line):
                if  k != 0:
                    node, distance = val.split(',')
                    adj_l.append((int(distance),int(node)))
                    #print("k is : {}, val is {}".format(k, val))
            network.append(adj_l)
            
    network.insert(0,[])
    return network
    
def print_network(network):
    print("\ngraph (distance,node) :")
    for k, adj_l in enumerate(network):
        if k != 0:
            print(adj_l)
    print("\n")
    return


DATA = sys.argv[1]
SOURCE = 1
END = int(sys.argv[2])

network = read_in_network(DATA)

# validate this is a node in the network
assert END <= (len(network)-1)

#print_network(network)

num_nodes = len(network) - 1


best_paths = [1000000 if k != SOURCE else 0 for k in range(num_nodes+1)]
visited = [False for k in range(num_nodes+1)]

heap = [(0, SOURCE)]

while heap :
    dist, node = hq.heappop(heap)
    
    if (visited[node] == True):
        continue
    
    best_paths[node] = dist
    visited[node] = True
    
    for weight, neighbor in network[node]:
        if visited[neighbor] == False :
        #if ((weight + dist) < best_paths[neighbor]):
            hq.heappush(heap, (weight+dist, neighbor))


#print("Best paths from Node {} are \n{}".format(SOURCE, best_paths))

print("\nBest path from Node {} to Node {} is {}".format(SOURCE,END,best_paths[END]))