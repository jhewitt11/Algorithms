import sys
import heapq as hq

'''
For (weight - length) as calculation, ties going to higher weight, answer is 69113766264

For (weight / length) as calculation, ties arbitrary, answer is 67309413663
'''

def read_in_tasks(DATA):   
    tasks = []   
    with open(DATA, 'r') as f:

        for line in f:
            line = line.split()
            
            if len(line) == 2 :
                line = [int(k) for k in line]
                weight, length = line
                
                #score = weight / length
                score = weight - length
                hq.heappush(tasks,(-score, weight, length))
    return tasks
    
    

DATA = sys.argv[1]
tasks = read_in_tasks(DATA)

w_sum = 0
C = 0
buffer_score = False
buffer = []

while tasks :
    
    score, weight, length = hq.heappop(tasks)
    score = -score
    
    
    if score == buffer_score:
        hq.heappush(buffer, (-weight, length, score))
        
  
    else:
        for k in range(len(buffer)):
            cur_weight, cur_length, cur_score = hq.heappop(buffer)
            cur_weight = -cur_weight
                       
            C += cur_length

            w_sum += (cur_weight*C)
        
        buffer_score = score
        hq.heappush(buffer, (-weight, length, score))
        
for k in range(len(buffer)):
    cur_weight, cur_length, cur_score = hq.heappop(buffer)
    cur_weight = -cur_weight
               
    C += cur_length

    w_sum += (cur_weight*C)
        
print(" weighted completion sum : {}".format(w_sum))

