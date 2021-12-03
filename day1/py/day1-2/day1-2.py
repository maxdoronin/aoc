with open('day1/input.txt') as f:
    lines = f.readlines()

    counter = 0
    
    if len(lines) < 4:
        print (counter)
        exit

    depth0 = int(lines.pop(0)) + int(lines[0]) + int(lines[1])

    while len(lines) > 2:
        depth = int(lines.pop(0)) + int(lines[0]) + int(lines[1])
        if (depth > depth0):
            counter += 1
        depth0 = depth
    print (counter)