#function to evaluate minimal number of frog jumps

def solution(X, Y, D):
    jumps = 0
    subcheck = (Y - X) % D
    if subcheck != 0:
        jumps += 1
    jumps += (Y - X) // D
    return jumps

X = 10
Y = 50
D = 10

print(solution(X, Y, D))
