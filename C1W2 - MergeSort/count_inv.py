import numpy as np
import math

with open('IntegerArray.txt', 'r') as f:
    array = [ int(line) for line in f]

def split_array(array):
    '''
    Split array and return both halves.
    '''
    
    l = len(array)
    a = array[:math.ceil(l/2)]
    b = array[math.ceil(l/2):]
    
    return a, b

def merge_count_inv(a, b):
    '''
    Merge a and b, and count inversions.
    '''

    c = []
    inv = 0
    
    for k in range(len(a) + len(b)):
        
        if( len(a) == 0 ):
            c = c + b
            return c, inv
            
        if( len(b) == 0 ):
            c = c + a
            return c, inv
        
        if( a[0] <= b[0]):
            c.append(a.pop(0))

        else :
            inv += len(a)
            c.append(b.pop(0))
    
    return c, inv

def sort_count_inv( array ):
    '''
    Recursive merge sort implementation.
    
    Returns sorted array and number of inversions required.
    '''
    
    if(len(array) == 1):
        return array, 0
    
    a, b = split_array(array)
    
    a_sort, a_count = sort_count_inv(a)
    b_sort, b_count = sort_count_inv(b)
    
    c, merge_count = merge_count_inv(a_sort, b_sort)
    
    total = a_count + b_count + merge_count
    
    return c, total


test = [6, 5, 4, 3, 2, 1]

c, total = sort_count_inv(array)

#print("test is \t{}".format(test))
print("c is \t\t{}".format(c[0:50]))
print("total is {}".format(total))