import numpy as np
import math

entry1 = 3141592653589793238462643383279502884197169399375105820974944592
entry2 = 2718281828459045235360287471352662497757247093699959574966967627

def m_calc(num1, num2):
    '''
    Calculate the number of digits in the smallest number.
    '''

    if num1 <= num2:
        m = math.floor(len(str(num1))/2)
    else:
        m = math.floor(len(str(num2))/2)

    return m

def m_split(num, m):
    '''
    Split num in two. Return both parts.
    
    top : most significant len(num) - m digits
    bot : least significant m digits
    '''
    
    top = str(num)[:-m]
    bot = str(num)[len(str(num))-m:]
    
    return int(top), int(bot)

def k_mult( num1, num2):
    '''
    Recursive Karatsuba implementation.
    '''

    if( (num1 < 10) or (num2 < 10)):
        return num1 * num2
    
    m = m_calc(num1, num2) 
    
    a, b = m_split(num1, m)
    c, d = m_split(num2, m)
    
    AC = k_mult(a, c)
    BD = k_mult(b, d)
    inter = k_mult((a+b),(c+d)) - AC - BD
    
    return AC*(10**(m*2))+inter*(10**m)+BD

answer = k_mult(entry1, entry2)

print("answer is : {}".format(answer))

'''
test = 12
m = m_calc(test, test)

print("result is {}".format(m_split(test, m)))
'''