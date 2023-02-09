import numpy as np
import random
import math
import sys

def swap(array, i, j):
    '''
    Swap elements i and j in array.
    '''
    
    ph = array[i]
    array[i] = array[j]
    array[j] = ph
    
    return array

def parti(array, l, r):
    '''
    Build partially sorted partition around pivot and count swaps.
    '''
    i = l+1
    pivot = array[l]

    for j in range(l+1,r):
        if array[j] < pivot :
            array = swap(array, i, j)
            i += 1
    
    result = swap(array, l, i-1)

    return result, i-1

def choosePivot(array, num):
    '''
    Pivot Selection
    0 : first element
    1 : random element
    2 : last element
    3 : median of first, middle, last
    '''

    if num == 1:
        return random.randint(0,len(array)-1)
    if num == 0:
        return 0
    if num == 2:
        return len(array)-1
    if num == 3:
        first = array[0]
        last = array[-1]
        mid = array[math.floor((len(array)-1)/2)]
        
        median = int(np.median([first,mid,last]))
        
        if median == first:
            return 0
        elif median == mid:
            return math.floor((len(array)-1)/2)
        else :
            return -1

def quickSort(array):
    '''
    Recursive quickSort implementation. 
    
    Allows multiple strategies for selecting pivots.
    
    Returns sorted array and number of comparisons.
    '''

    if len(array) < 2 :
        return array, 0
   
    ## select pivot choice here
    p = choosePivot(array,3)

    array = swap(array, 0, p)
    array, piv = parti(array, 0, len(array))
       
    left, l_comps = quickSort(array[0:piv])
    right, r_comps = quickSort(array[piv+1:])

    comps = len(array)-1
    t_comps = comps + l_comps + r_comps

    return left+[array[piv]]+right, t_comps


#array = [5, 9, 3, 0, 4, 6, 2, 8, 1, 7, -1, 35, 42, 22, -43, 200, 11, 13]

DATA = sys.argv[1]

with open(DATA, 'r') as f:
    array = [ int(line) for line in f]
    
    
    
print("length of array is :",len(array))
answer, comps = quickSort(array)
print("answer is :",answer[:10])
print("comps is :", comps)
