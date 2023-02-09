import sys
import collections

def hamming_dist(A, B):
    xor = bin(A^B)
    dist = 0
    
    for ele in xor : 
        if ele == '1':
            dist += 1
            
    return dist 

def read_in_distances(DATA):  
    
    with open(DATA, 'r') as f:

        header = f.readline()
        header = header.split()
        num_nodes = int(header[0])
        digits = int(header[1])

        leaders = [ False for k in range(num_nodes)]
        clusters = [False for k in range(num_nodes)]
        indices = {}
        codes = []

        for k, line in enumerate(f):
            num = int(''.join(line.split()),2)
            codes.append(num)        
            
            if indices.get(num) != None:
                indices[num].append(k)
                leaders[k] = indices[num][0]
                clusters[indices[num][0]].append(k)
                
            else :
                indices[num] = [k]
                leaders[k] = k
                clusters[k] = [k]

    return num_nodes, digits, codes, indices, leaders, clusters
  
def create_hamming_candidates(code, digits):

    can_l = [] 
    
    for k in range(digits):
        
        candidate_s = code ^ (1 << k)
        can_l.append(candidate_s)
        
        for i in range(digits):
            candidate_d = candidate_s ^ (1 << i)
            can_l.append(candidate_d)      
        
    can_l = set(can_l)
    can_l.remove(code)
    can_l = list(can_l)
    
    return can_l


def cluster_codes(num_nodes, digits, codes, indices, leaders, clusters):

    num_clusters = 0

    for A_ind, code in enumerate(codes) : 
        candidates = create_hamming_candidates(code, digits)
        
        for candidate in candidates:
            matches = indices.get(candidate)
            
            if (matches == None):
                continue
            
            B_ind = matches[0]
            if (leaders[A_ind] == leaders[B_ind]):
                continue
            
            A_ind = leaders[A_ind]
            B_ind = leaders[B_ind]
            
            #swap so A always takes B
            if len(clusters[A_ind]) < len(clusters[B_ind]):
                mid = A_ind
                A_ind = B_ind
                B_ind = mid               
            
            for follower in clusters[B_ind]:
                leaders[follower] = A_ind
            
            clusters[A_ind] += clusters[B_ind]
            clusters[B_ind] = False

    for k in clusters:
        if k != False:
            num_clusters += 1

    return leaders, clusters, num_clusters

DATA = sys.argv[1]
num_nodes, digits, codes, indices, leaders, clusters = read_in_distances(DATA)

print("\nnum_nodes is {}, digits is {}, length of codes, indices is {}, {}\n".format(num_nodes, digits, len(codes), len(indices)))

leaders, clusters, num_clusters = cluster_codes(num_nodes, digits, codes, indices, leaders, clusters)

print("\nnumber of clusters is : ", num_clusters)