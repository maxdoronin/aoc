with open('../../input.txt') as f:
    lines = f.readlines()

    counter = 0

    if len(lines) < 2:
        print (counter)
        exit

    depth0 = int(lines.pop(0))

    for line in lines:
        depth = int(line)
        if (depth > depth0):
            counter += 1
        depth0 = depth
    print (counter)