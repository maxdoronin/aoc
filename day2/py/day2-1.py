with open('../input.txt') as f:
    lines = f.readlines()

    hposition = 0
    vposition = 0

    for line in lines:
        (command, value) = line.split()
        intvalue = int(value)
        if command == 'down':
            vposition += intvalue
        elif command == 'up':
            vposition -= intvalue
        else:
            hposition += intvalue

    print (hposition)
    print (vposition)
    print (hposition*vposition)