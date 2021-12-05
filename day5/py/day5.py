def read_input(file_name):
    with open(file_name) as f:
        lines = f.readlines()
        vents = []
        for line in lines:
            vents.append ([[int(coord)  for coord in point.split(',')] for point in line.strip().split(' -> ')])
        return (vents)

def initialize_map(vents):
    map_size = max([max(max(vents[i][0]), max(vents[i][1])) for i in range (len(vents))]) + 1
    map = [[0]*map_size for i in range(map_size)]
    return(map)

def map_vents(vents, map, consider_diagnoals=False):
    for vent in vents:
        hdelta = vent[1][0] - vent[0][0]
        vdelta = vent[1][1] - vent[0][1]
        h0 = vent[0][0]
        h1 = vent[1][0]
        v0 = vent[0][1]
        v1 = vent[1][1]
        hstep = 0
        if hdelta != 0:
            hstep = hdelta // abs(hdelta)
        vstep = 0
        if vdelta != 0:
            vstep = vdelta // abs(vdelta)
        if not consider_diagnoals and (hdelta != 0 and vdelta != 0):
            continue
        h = h0
        v = v0
        while abs(h1 - h) + abs(v1 - v) != 0:
            map[v][h] += 1
            h += hstep
            v += vstep
        # below line handles 'dots' and the last points
        map[v][h] += 1

def count_overlaps(map):
    return (sum([sum (x>1 for x in map[i]) for i in range(len(map))]))


print('Part 1')
vents = read_input('testinput.txt')
map = initialize_map(vents)
map_vents(vents, map)
print(count_overlaps(map))

vents = read_input('input.txt')
map = initialize_map(vents)
map_vents(vents, map)
print(count_overlaps(map))

print('Part 2')
vents = read_input('testinput.txt')
map = initialize_map(vents)
map_vents(vents, map, consider_diagnoals=True)
print(count_overlaps(map))


vents = read_input('input.txt')
map = initialize_map(vents)
map_vents(vents, map, consider_diagnoals=True)
print(count_overlaps(map))