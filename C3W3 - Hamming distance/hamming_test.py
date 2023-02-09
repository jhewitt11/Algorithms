

def create_hamming_candidates(code):

    can_l = []
    length = len(bin(code))-2    
    
    for k in range(length):
        
        candidate_s = code ^ (1 << k)
        can_l.append(candidate_s)
        
        for i in range(length):
            candidate_d = int(candidate_s) ^ (1 << i)
            can_l.append(candidate_d)      
        
    can_l = set(can_l)
    can_l.remove(int(code))
    can_l = list(can_l)
    
    return can_l


code = int('1100',2)

answer = create_hamming_candidates(code)

for code in answer :
    print("code is : {}, binary is {}".format(code, bin(code)))


print("code is ", code)
print("bin(code) is ", bin(code))