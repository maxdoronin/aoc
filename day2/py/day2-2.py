with open('../input.txt') as f:
    lines = f.readlines()

    hposition = 0
    vposition = 0
    aim = 0

    for line in lines:
        (command, value) = line.split()
        intvalue = int(value)
        if command == 'down':
            aim += intvalue
        elif command == 'up':
            aim -= intvalue
        else:
            hposition += intvalue
            vposition += aim*intvalue

    print (hposition)
    print (vposition)
    print (hposition*vposition)