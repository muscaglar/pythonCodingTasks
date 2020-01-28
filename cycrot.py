#A program to cycle/rotate a list to the right, taking the final element and appending it at the beginning

def solution(A, K):
    i = 0
    if len(A) == 0:
        return A
    else:
        while i < K:
            A.insert(0, A[-1])
            del(A[-1])
            i += 1
        return A

A = [1, 2]
K = 5

print solution(A, K)
