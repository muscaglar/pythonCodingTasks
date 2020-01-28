#Simple program to print all numbers 1-100, with usual Fizz/Buzz rules

for x in xrange(1,101):
    output = ''

    if x % 3 == 0:
        output += 'Fizz'
    if x % 5 == 0:
        output += 'Buzz'
    if output == '':
        output = x
    print(output)
