import sys

f = open(sys.argv[1])
file = f.readlines()

curr = 0

variables = dict()
def setv(line):
    if len(line) > 1:
        if len(line) > 2:
            variables[line[1]] = eval(line[2])
        else:
            variables[line[1]] = eval('0')

def printv(line):
    if len(line) == 2:
        if line[1] in variables:
            print(variables[line[1]])
        else:
            print(line[1])

def ifv(line):
    if len(line) > 1:
        return 1^int(eval(line[1]))

while curr < len(file):
    line = file[curr]
    line = line[:-1]
    line = line.split(' ')
    match line[0]:
        case 'set':
            setv(line)
        case 'if':
            curr += ifv(line)
        case 'out':
            printv(line)
        case 'jmp':
            if len(line) > 1:
                curr = int(line[1])-2
    curr += 1
