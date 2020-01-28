'''import math

pi = '3.123456789112345678921234567893'
placeno = 0
while True:
    placeno = input('Enter required decimal place of Pi: ')
    if placeno < 30:
        print pi[:(placeno + 2)]
        False
    else:
        print "That's too much Pi... Try again?"


#Optional: convergence series to calculate Pi (note, T = O(N))
#n = input('Enter pi to the desired number of decimal places: ')
n = int(100)
picount = 0
i = 1.0

while (i <= n):
    if(i % 2 != 0):
        picount += (1.0/(2.0*i - 1))

    if(i % 2 == 0):
        picount -= (1.0/(2.0*i - 1))

    i += 1
#print (4.0*picount)
'''
'''
val = input('Would you like the Fibonaci sequence to the nth number? (1) or to the value closest to which you enter? (0) \n')
a, b = 0, 1
if val == 1:
    N = input('Enter desired nth value of Fibonaci sequence: \n')
    for i in xrange(N-2):
        a, b = b, a+b
    print b
if val == 0:
    N = input('Enter desired value to match closest to Fibonaci sequence: \n')
    while b < N:
        a, b = b, a+b
    if ((b - N) < (N - a)):
        print 'Closest Fibonaci number: ', b
    else:
        print 'Closest Fibonaci number: ', a
else:
    print "You didn't enter 0 or 1, try again?"
'''
'''
A = [0, 1, 2, 9, 4, 6, 6, 1, 4, 7, 8, 9]
print len(set(A))
'''
'''
prod = 1
A = [0, 1, 2, 9, 4, 6, 6, 1, 4, 7, 8, 9] 
for i in range(3):
    prod *= max(A)
    A.remove(max(A))
print prod

def solution(A):
    A.sort()
    return max(A[0]*A[1]*A[-1], A[-1]*A[-2]*A[-3])
'''
'''
A = [10, 2, 5, 1, 8, 20]
A.sort()
a = b = c = 0
print A
for i in reversed(A):
    a, b, c = i, a, b
    if a + b > c and a + c > b and c + b > a:
        print 1
        quit()
    else:
        print 0
'''
'''
A = [0, 1, 0, 0, 1, 0, 0]
n = len(A)
size, result = 0, 0 
for i in xrange(n):
    if A[i] == 0: 
        size += 1
    else:
        size -= 1
        result = max(result, -size)
print result
'''
'''
S = '{[]}'
check = ['{', '[', '(']
closer = {'}':'{', ']':'[', ')':'('}
stack = []

for brak in S:
    if brak in check:
        stack.append(brak)
        print 'Added:', brak, 'stack:', stack
    else:
        if len(stack) == 0:
            print 'Stack killed; not nested'
        elif closer[brak] != stack.pop():
            print 'Last bracket not matched to closer: removed'
    if len(stack) == 0:
        print 'stack empty'
    else:
        print 'Stack filled:', stack
'''
'''
A = [4, 3, 2, 1, 5]
B = [0, 1, 0, 0, 0]
i = 0

while i < len(A): #less than as i starts on 0 and length is mod
    print i
    if B[i] == 1 and B[i+1] == 0:
        if A[i] < A[i+1]:
            A.pop(i)
            B.pop(i)
            continue
        else:
            A.pop(i+1)
            B.pop(i+1)
            continue
        print A, B
    if B[i-1] == 1 and B[i] == 0 and i+1 == (len(A)):
        i -= 1
        pass
    else:
        print 'None eaten', A, B
        i += 1
'''
'''
A = [4, 3, 2, 1, 5]
B = [0, 1, 0, 0, 0]
alive = 0
downstream = []

for i in xrange(len(A)):
    print 'i = ', i, 'A[i] =', A[i], 'B[i] =', B[i]
    if B[i] == 1:
        downstream.append(A[i])
        print 'B = 1:', downstream
    else:
        print 'B = 0. Check...'
        while len(downstream) != 0:
            if downstream[-1] < A[i]:
                downstream.pop()
                print 'Down eaten:', downstream
            else:
                print 'Up eaten:', downstream
                break
        else:
            alive += 1
            print 'Alive total:', alive
alive += len(downstream)
print 'Final alive:', alive
'''
'''
S = '(()(())())'
open = []

N = '(()()))'
N2 = '(()'

for brak in S:
    print 'Braket:', brak
    if brak == '(':
        open.append(brak)
        print 'Brak open:', open
    else:
        while len(open) != 0:
            print 'Open queued:', open
            if open[-1] != brak:
                open.pop()
                print 'Braket closed:', open
                break
            else:
                print 'Another opened, return to start...'
                break
if brak == ')' and len(open) == 0:
    return 0
elif len(open) != 0:
    return 0
else:
    return 1
'''
'''
S = ')('

nestcount = 0

for brak in S:
    if brak == '(':
        nestcount += 1
    else:
        nestcount -= 1
        if nestcount < 0:
            print 'Not nested'

    if nestcount == 0:
        print 'Nested correctly'
    else:
        print 'Not correct, end'
'''
'''
A = [4, 2, 4, 2, 4, 2, 4, 9, 4, 6, 4, 1, 4]
stack = []
i = 0
checker = 1
count = 0
while i < (len(A)-1):
    stack.append(A[i])
    print 'A[i] =', A[i], 'i = ', i, 'stack: ', stack
    if A[i+1] != stack[-1]:
        stack.pop()
        i += 2
        if count == A[i]:
            checker += 1
    else:
        i += 1
        continue
    count = A[i]
if len(set(stack)) == 1 or checker == (len(A)/2):
    print 'Leader found: '
else:
    print 'No leader', checker
'''

#create stack, add numbers sequentially, and check stack for leader each time one is added
#if leader exists in stack, check remaining list for leader
#if remaining list has leader, count += 1
'''
A = [4, 3]
equilead = []
counter = [0]*(max(A)+1)
equi = 0

for i in xrange(len(A)):
    equilead.append(A[i])
    counter[A[i]] += 1
    print 'i = ', i, 'A[i] =', A[i], 'stack =', equilead, 'Cnt =', counter
    if any ( var > (float(len(equilead))/2) for var in counter):
        print 'Leader found:', counter.index(max(counter))
        print A[(i+1):], len(A[(i+1):])
        if A[(i+1):].count(counter.index(max(counter))) > float(len(A[(i+1):])/2):
            print 'Equi-leader found!'
            equi += 1
print equi
'''

#Simple loop to find a leader in a list
'''
A = [4, 2, 4, 2, 4, 4]

leng = len(A)
lead = 0
lead_count = 0
lead_index = 0

for i in xrange(leng):
    if lead_count == 0:
        lead = A[i]
        lead_index = i
        lead_count += 1
    else:
        if A[i] == lead:
            lead_count += 1
        else:
            lead_count -= 1

#now count leaders:
lead_count = len([number for number in A if number == lead])
if lead_count <= leng//2:
    print 'Not a leader'

#Now, using sums, check implicitly for leaders in either side of the stack
first_lead = 0
last_lead = 0
equi = 0

for i in xrange(leng):
    if A[i] == lead:
        first_lead += 1
    if first_lead > (i+1)//2 and (lead_count - first_lead) > (leng - (i+1))//2:
        equi += 1
print equi
'''

#Finding the dominator and returning any index with its value (virtually identical to above)
'''
A = [3, 2, 3, 2, 4, 3, 3, 5, 3]

dom_count = 0
dom_cand = 0
dom_ind = 0

for i in xrange(len(A)):
    if dom_count == 0:
        dom_cand = A[i]
        dom_ind = i
        dom_count += 1
    else:
        if A[i] == dom_cand:
            dom_count += 1
        else:
            dom_count -= 1

leaders = []

for i in xrange(len(A)):
    if A[i] == dom_cand:
        leaders.append(i)
if len(leaders) > len(A)//2:
    print 'Dominator exists:', dom_cand, '\n', 'Dominator indices:', leaders
'''

#Return the greatest possible profit from a stock given a log of it's former daily prices
'''
A = [121, 141, 132, 137, 138, 110] 
pprof = 0
profit = 0
i = 0
while i == 0:
    maxp = max(A)
    maxi = A.index(max(A))
    minp = min(A)
    mini = A.index(min(A))

    if mini > maxi:
        A.pop(mini)
        continue
    else:
        profit = maxp - minp
        if pprof > profit:
            print pprof
            i = 1
        else:
            pprof = profit
'''
'''
#while loop not breaking properly above, correct? Attempting for loop below...

A = [0, 0, 0, 0, 0, 0]
pmin = A[0]
prof = 0
prof_i = 0

for i in xrange(len(A)):
#Seek minimum value
    if pmin > A[i]:
        pmin = A[i]
#Find difference between A[i] and current lowest value
    else:
        prof_i = A[i] - pmin
#Seek greatest profit
    if prof_i > prof:
        prof = prof_i
    else:
        continue

print prof
'''

A = [-6, -2, -4, -1, -2]
sum = A[0]
cand = []

for i in xrange(1, len(A)):
    if (A[i] + sum > sum):
        sum += A[i]
    else:
        if A[i] > sum:
            sum = A[i]
            cand.append(sum)
        else:
            cand.append(sum)
            sum = 0
    print i, A[i], sum, cand
cand.append(sum)

print max(cand)
