import heapq
import sys

class maximum_heap():
    '''
    Heap that returns maximum number not minimum.
    '''

    def __init__(self, li = None):  
        if li:
            heapq.heapify(li)
            self.heap = li
        else:
            self.heap = []
        
        return
        
    def __len__(self,):     
        return len(self.heap)
        
    def __getitem__(self, ind):
        return self.heap[ind] * -1
          
    def heappush(self, num):
        heapq.heappush(self.heap, num * -1)
        return
        
    def heappop(self,):
        return heapq.heappop(self.heap) * -1
        

# read in data
def read_in_data(DATA):
    
    with open(DATA) as file:       
        array = [int(x) for x in file]
            
    return array


# Balance min and max heaps, won't correct if out of place
# Returns : min_heap, max_heap
def balance_heaps(min_heap, max_heap):
    
    diff = len(max_heap) - len(min_heap)
    
    while diff > 1:
        
        num = max_heap.heappop()
        heapq.heappush(min_heap, num)
        
        diff -= 2
    
    while diff < -1:
        
        num = heapq.heappop(min_heap)
        max_heap.heappush(num)
        
        diff += 2

    return min_heap, max_heap


# Adds num correctly to two heap system and balances
# Returns : min_heap, max_heap
def add_return(min_heap, max_heap, num):

    if (len(min_heap)) == 0 or (len(max_heap) == 0):
        max_heap.heappush(num)
    
    else:
        if num <= max_heap[0]:
            max_heap.heappush(num)
            
        elif num >= min_heap[0]:
            heapq.heappush(min_heap, num)
            
        else:
            if len(min_heap) < len(max_heap):
                heapq.heappush(min_heap, num)
            
            else :
                max_heap.heappush(num)

    min_heap, max_heap = balance_heaps(min_heap, max_heap)
    
    return min_heap, max_heap


# Returns median from balanced two heap system. If even, returns smallest
def pull_median(min_heap, max_heap):
   
    if len(min_heap) > len(max_heap):
        median = min_heap[0]
        
    else:
        median = max_heap[0]

    return median


def kth_median(array, k):
    #pull_median(min_heap, max_heap) -> median
    #add_return(min_heap, max_heap, num) -> min_heap, max_heap
    
    if len(array) < k: 
        print(f'k : {k}, larger than array length : {len(array)}')
        return None
    
    min_heap = []
    max_heap = maximum_heap()
    
    # add k elements from array to two heap system
    for i in range(k):
        min_heap, max_heap = add_return(min_heap, max_heap, array[i])
        
    # pull median after k elements added
    median =  pull_median(min_heap, max_heap)
    print(f'k : {k}, kth median : {median}')
    
    return median
    
    
array = read_in_data(sys.argv[1])

median = kth_median(array, 30)


# This can be deleted. Only for testing.
li = [5, 4, 3]
max_heap = maximum_heap(li)

min_heap = [20,19,18,17,16,15,14]
heapq.heapify(min_heap)

min_heap, max_heap = balance_heaps(min_heap, max_heap)
