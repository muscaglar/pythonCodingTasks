#List of class defintions for subsequent data analysis

#Example set of first three for testing:
#Name of file: example.txt

#Print's line if relevant (switch to '0' for irrelevance)
'''
with open("example.txt", 'r') as f:
    for line in f.readlines():
        if line.startswith('1'):
            print line
'''
#queryret = input("Enter Query ID:")
'''
getqid = input('Enter QID:')

with open("example.txt", 'r') as f:
    for line in f.readlines():
        if line.startswith('1') and getqid in line:
            print(line)
'''
#Data extraction method
'''
with open("example.txt", 'r') as f:
    for line in f.readlines():
        if line.startswith('1'):
            passer = line
            passer = passer[15:]
            #Strip first characters in arg from beginning: passer = line.lstrip('1 qid:')
            #Remove whitespace and delete last three char: passer = passer.replace(' ','')[:-3]
            passer = passer[:-24]
            passer = passer.replace(' ', '\n')
           # passer = passer.replace(' ', '\n')
            passer = passer.split(':', 1)[-1]
            print(passer)
'''

d = {'1': [], '2': [], '3': [], '4': [], '5': [], '6': [], '7': [], '8': [], '9': [], '10': [], '11': [], '12':[], '13': [], '14': [], '15': [], '16': [], '17': [], '18': [], '19': [], '20':[], '21': [], '22': [], '23': [], '24': [], '25': [], '26': [], '27': [], '28': [], '29': [], '30': [], '31': [], '32': [], '33': [], '34': [], '35': [], '36': [], '37': [], '38': [], '39': [], '40': [], '41': [], '42': [], '43': [], '44': [], '45': [], '46': [], '47': [], '48': [], '49': [], '50': [], '51': [], '52': [], '53': [], '54': [], '55': [], '56': [], '57': [], '58': [], '59': [], '60': [], '61': [], '62': [], '63': [], '64': []}
'''
getqid = input('Enter QID:')

with open("test.txt", 'r') as file, open("output.txt", 'w') as file2:
    for line in file:
        if line.startswith('1') and getqid in line:
            data = line[15:-24]
            data = data.rstrip().split()
        
            for elem in data:
                (name, value) = elem.split(':')
                d[name].append(value)

    for k in sorted(d):
        file2.write('\t'.join(d[k]) + '\n')

'''

qidtoken = 170
getqid = 'WT04-' + str(qidtoken)

with open("example.txt", 'r') as file:

    while qidtoken < 221:
        
        filename = 'rel' + str(qidtoken) + '.txt'
        output = open(filename, 'w')

        for line in file:
            if line.startswith('1') and getqid in line:
                data = line[15:-24]
                data = data.rstrip().split()
            
                for elem in data:
                    (name, value) = elem.split(':')
                    d[name].append(value)
        
        for k in sorted(d):
            output.write('\t'.join(d[k]) + '\n')
        output.close()
        qidtoken += 1
