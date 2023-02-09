#from quickSort import quickSort
import math
import sys


def is_match(x, y):
    if abs(x + y) <= 10000:
        return True
    else:
        return False

def expand_search(k, x_ind, array):
        
    matches = []   
    
    success = 1 
    cur = x_ind
    
    while (cur <= len(array)-1) and success == 1 :
        if is_match(k, array[cur]) == True:
            matches.append(k+array[cur])
            cur += 1
        else:
            success = 0
    
    success = 1
    cur = x_ind
    while (cur >= 0) and success == 1 :
        if is_match(k, array[cur]) == True:
            matches.insert(0, k+array[cur])
            cur -= 1
        else:
            success = 0

    return matches


def binary_search(k, array):

    l_bound = 0
    r_bound = len(array)-1
    cur = int(len(array)/2)
    
    x = array[cur]
    
    while (is_match(x, k) == False):
        
        if abs(l_bound - r_bound) < 2:
            return expand_search(k, l_bound, array) 
        
        if x+k > 10000:
            r_bound = cur   
        else:
            l_bound = cur
        
        cur = int((r_bound + l_bound)/2)
        x = array[cur]
    
    return expand_search(k, cur, array)




DATA = sys.argv[1]
with open(DATA, 'r') as f:
    array = [ int(line) for line in f]

array = sorted(array)

found_sums = []
for k in array :

    results = binary_search(k, array)
    if results :
        found_sums += results
    
found_sums = set(found_sums)
print("# of unique 2sums are : {}".format(len(found_sums)))
#print("found sums are : ", found_sums)