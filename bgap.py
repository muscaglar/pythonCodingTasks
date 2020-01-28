N = input('Enter number for binary count: ')

A = (bin(N))[2:]
length = len(A)
list = []
counter = 0
trigger = 0
i = 0

print "A = ", A, ": ", "Length = ", length, ": ", "List =", list

while (i < length):
    if (A[i] == '1' and trigger == 0):
        trigger = 1
    if(trigger == 1):
        if(A[i] == '0'):
            counter += 1
        else:
            list.append(counter)
            counter = 0
    print "i = ", i, ", ", "counter = ", counter, ", ", "trigger = ", trigger
    i += 1
print max(list), list
