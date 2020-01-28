#Working out the odd element in an array of pairs                                                                                  
#Alternative solution                                                                                                              
'''                                                                                                                                
A = [2, 4, 5, 2, 4, 5, 7]                                                                                                          
def solution(A):                                                                                                                   
    result = 0                                                                                                                     
    for number in A:                                                                                                               
        result ^= number                                                                                                           
                                                                                                                                   
    return result                                                                                                                  
                                                                                                                                   
print solution(A)                                                                                                                  
'''
#My solution: 44%                                                                                                                  
'''                                                                                                                                
A = [2, 6, 9, 6, 2]                                                                                                                
n = len(A)                                                                                                                         
count = 0                                                                                                                          
odd = 0                                                                                                                            
                                                                                                                                   
def solution(A):                                                                                                                   
    n = len(A)                                                                                                                     
    count =0                                                                                                                       
    odd = 0                                                                                                                        
                                                                                                                                   
    for i in xrange(n):                                                                                                            
        for j in xrange(n):                                                                                                        
            if A[i] == A[j]:                                                                                                       
                            count += 1                                                                                             
        if count == 1:                                                                                                             
            odd = A[i]                                                                                                             
        count = 0                                                                                                                  
    return odd                                                                                                                     
    pass'''

