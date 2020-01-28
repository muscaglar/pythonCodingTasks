string = "Hello, world!"

#print string
#print string[3:]
#print string[2:7]
#print string[:9]
#print string * 2
#print string + "small appendix"
'''
list = [ 'element 0', 1, 2.0, 'three']
tinylist = [ 'just me' ]
'''
#print list
#print list[0]
#list[2] = 'just two now'
#print list[2:]
#print list[1:2]
#print list + tinylist

tuple = ( 0, 1.0, 'two' )
tinytuple = ( 47, 47 )
#no single element list/tuples will default to int/str

#print tuple
#print tuple[2]
#print tuple[1:]
#print tuple * 3
#print tuple + tinytuple

dict = {1 : 'entry one', 2 : 'second element' , 3 : '3rd entry'}
tinydict = {}
tinydict[1] = 'This is value 1'
tinydict['two'] = 'This is value 2'

#print dict
#print dict[1]
#print dict.keys()
#print dict.values()
#print tinydict

#This is a list of functions

#Converting string to integer (or float)
x = '267100'
y = int(x)
#print y

#Turns each digit in x to a float list
float_x = [float(a) for a in x]
#print float_x

#create complex number (must be same type throughout)
i = complex(y, 3)
#print i

#More complicated: function defintion to return objects for strings
'''
def evaluator(x):

    if isinstance(x, str):
        j = eval(x)

    else:
        j = "Argument is not a string, try again?"

        return j

#print (evaluator(x))
'''
#Turn a number into a binary one
k = bin(y)
#print k

#Simple Operators
a = 40
b = 4
c = 7

#operators = {'divide':a/c, 'exp':c**a, 'multi':b*c, 'floor': a//c, 'modu':c%b}
#print operators.values()

#Comparison Logic Operators

'''if ( a == b ): #equality condition
   print "Line 1 - a is equal to b"
else:
   print "Line 1 - a is not equal to b"

if ( a != b ): #anti-equality condition (true if not equal)
   print "Line 2 - a is not equal to b"
else:
   print "Line 2 - a is equal to b"

if ( a <> b ): #anti-equality
   print "Line 3 - a is not equal to b"
else:
   print "Line 3 - a is equal to b"

if ( a < b ): #less than
   print "Line 4 - a is less than b" 
else:
   print "Line 4 - a is not less than b"

if ( a > b ): #greater than
   print "Line 5 - a is greater than b"
else:
   print "Line 5 - a is not greater than b" '''

#Assignment Operators: loop to tell you the difference between two numbers
#c += a does c = c + a, -= subtracts, *= multiplies, /= divides and so on
'''
no1 = input('Enter start number: ')
no2 = input('Now enter the final number: ')
i = 0

if(no1 > no2):
    print "Nope! Start number larger than end!"
if(no1 < no2):
    while(no1 < no2):
        no1 += 1
        i += 1
    else:
        print 'Start number now equals %d (end) which is a difference of %d ' % (no1, i) '''

#Nested loops
'''
n = input('How many lines of stars do you want?')

for i in range(1, n + 1):     #creates int i to loop between two values, 1 and n
    for j in range(i):        #creates int j to loop between 1 and i, printing as many *'s as i
        print '*', 
    print                     #prints a new line for the stars
'''
'''
n = input('Enter an integer to count the digits: ')
result = 0 
while n > 0:
    n = n // 10               #Floor division returns just the integers (necessary as using ints)
    result += 1               #Count how many times we're dividing
print result
'''

#Array search and return
#Function to find negative temperatures in an array of temp
'''
temperatures = [21, 15, 7, -3, -2, 4, 10, 14]
def negative(temperatures):     #Creating a function using the array  
    N = len(temperatures)       #find's length of array
    days = 0                    
    for i in xrange(N):         #i for each element, in the range of array's length
        if temperatures[i] < 0: 
            days += 1
    return days
print negative(temperatures)
'''

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
#My solution: 44%: Find the unpaired element
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
'''
A = [1, 2, 3, 4, 5]
k = 3
j = len(A)
for l in range(k-1):
    save = A[0]
    for i in xrange(j-1):
        A[i] = A[i + 1]
    A[j - 1] = save
print A
'''
'''
A = [2, 5, 3, 1, 4, 7]

B = 0
j = 1
N = len(A)
while (j <= N):
    for i in xrange(N):
        if (A[i] == j):
            j += 1
            break
        if (i == (N - 1) and A[i] != j):
            print j
            j = N + 1
        else:
            pass

A = [1, 2, 3, 5, 6, 7]

def solution(A):
    length = len(A)
    xor_sum = 0
 
    for i in range(0, length):
        xor_sum = xor_sum ^ A[i] ^ (i + 1)
 
    return xor_sum ^ (length + 1)
'''
'''
x = 1
y = 10
d = 1

delD = ((float(y) - float(x))/float(d))
intgap = 0
if ( delD % 1 != 0):
    intgap = (delD + 1)
else:
    intgap = delD
print int(intgap)
'''
'''
A = [1, 2, 3]
t = 0
while (t == 0):
    for i in xrange(len(A)):
        if (len(A) == 1):
            print A[i]
        if (A.count(i) == 0 and (i != 0)):
            odd = i
            t = 1
        else:
            pass
print i

for i in xrange(len(A) + 1):
    if (A.count(i) == 0 and (i != 0)):
        print 'i occurances = ', A.count(i), 'i = ', i
    if (len(A) == 1):
        print A[i]

A = [-1000, 1000]
totali = 0
sumlist = []
for i in xrange(1, len(A)):
    totali = abs(sum(A[i:]) - sum(A[:i]))
    sumlist.append(totali)
    print 'i down =', sum(A[:i]), ' i up  =', sum(A[i:]), 'diff =', totali
print min(sumlist)
'''
'''
def solution(A):
    leng = (len(A) + 1)
    occur = [False]*(leng)
    for i in A:
        if 1 <= i <= leng:
            occur[i - 1] = True
    for j in xrange(leng):
        if occur[j] == False:
            return (j + 1)

#Also, here:

def solution(a):
    return min(set(range(1, len(a) + 2)).difference(set(a)))
'''
'''
A = [1, 2, 4, 4]
leng = len(A)
if (set(range(1, len(A)+1))).issubset(set(A)) and max(A) == len(A):
    print 'all there'
else:
    print 'missing element(s)'

#minposdiff = min(C)
#print minposdiff
'''
'''
A = 3
B = 17
d = 3
print A % d, B % d
if A % d == 0:
    first = A
else:
    first = (A +(d - (A % d)))
if B % d == 0:
    last = B
else:
    last = (B - (B % d))
print first, last 

print ((last - first)/d + 1)
'''
'''
A = [0, 1, 0, 1, 1]
n = 0
for i in xrange(len(A)):
    if A[i] == 0:
        n += A[i:].count(1)
    if n > 1000000000:
        return -1
print n     
'''
'''
a = 1
b = 1
X = 10
i = 0
plusmin = []
while i == 0:
    a, b = b, a+b
    print 'a =', a, 'b =', b, X
    if X < b:
        plusmin.append(X - a)
        plusmin.append(b - X)
        print plusmin
        i = 1
'''
'''
A = [4600, 210, 20, 0, 180, 150, 290]
presum = A[0]
count = 0
B = sorted(A[1:])
print B

while (presum < 5000):
    for i in xrange(len(B)):
        presum += B[i]
        count += 1
        print presum, count

        #if presum > 5000:
        #print (count - 1)
'''
'''
A = [4600, 210, 20, 0, 180, 150, 290]
def solution(A):
    presum = A[0]
    count =0
    B = sorted(A[1:])

    for i in xrange(len(B)):
        presum += B[i]
        count += 1
        if presum > 5000:
            return (count - 1)
            break

print solution(A)
'''

#Die roll simulator
import random
raw_input("Welcome to the dice roll simulator... Press Enter to continue...")
sides = (input("How many sides would you like your dice?\n"))
raw_input("Excellent. Press Enter to roll...")

datum = open("Data dice", 'w')

sidelist = list(range(1, sides+1))
t = float(len(sidelist))

for i in xrange(1000):

    sidelist = list(range(1, sides+1))
    t = float(len(sidelist))

    while t > 1:
        if t % 2.0 != 0.0:
            x = random.random()
            if x < 0.5:
                midfl = (t/2 + 0.5) + 1
                mid = int(midfl)
                print 'odd, x < 0.5 mid:', mid
                if random.random() < 0.5:
                    del sidelist[mid:]
                else:
                    del sidelist[:(mid-1)]
            if x > 0.5:
                midfl = (t/2) + 0.5
                mid = int(midfl)
                print 'odd, x > 0.5 mid:', mid
                if random.random() < 0.5:
                    del sidelist[mid:]
                    print "higher del"
                else:
                    del sidelist[:mid]
                    print "lower del"
            else:
                continue
            print sidelist
        else:
            y = random.random()
            midfl = t/2
            mid = int(midfl)
            print 'even mid:'
            if y < 0.5:
                del sidelist[(mid):]
            if y > 0.5:
                del sidelist[:(mid)]
            print sidelist
        
        t = float(len(sidelist))
        print "dice list:", sidelist, "length:", t
    if t != 0:
        datum.write(str(sidelist[0]) + "\n")
