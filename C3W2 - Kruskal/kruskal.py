import sys
import heapq as hq

# answer with edges_data.txt and 4 clusters is 106

def read_in_distances(DATA):
    
    heap = []
    
    with open(DATA, 'r') as f:

        header = f.readline()
        num_nodes = int(header)

        for line in f:
            line = line.split()
            hq.heappush(heap, (int(line[2]),int(line[0]), int(line[1])))

    return num_nodes, heap
    
def greedy_clustering(K, num_nodes, heap):

    leaders = [i for i in range(num_nodes+1)]
    clusters = [[i] for i in range(num_nodes+1)]
    
    num_clusters = num_nodes
    
    while num_clusters != K:
        dist, A, B = hq.heappop(heap)
        
        if leaders[A] == leaders[B]:
            continue
        
        A = leaders[A]
        B = leaders[B]
        
        #swap so A cluster is always >=
        if len(clusters[A]) < len(clusters[B]):
            mid = A
            A = B
            B = mid
        
        for node in clusters[B]:
            leaders[node] = A
            
        clusters[A] += clusters[B]
        clusters[B] = False
        num_clusters -= 1

    dist, A, B = hq.heappop(heap)
    while leaders[A] == leaders[B]:
        dist, A, B = hq.heappop(heap)

    return dist, leaders, clusters, heap

DATA = sys.argv[1]
K = int(sys.argv[2])

num_nodes, heap = read_in_distances(DATA)

distance, leaders, clusters, heap = greedy_clustering(K, num_nodes, heap)

print("Distance is : ", distance)



#create leader array
#create cluster list of lists

#define stop condition, results