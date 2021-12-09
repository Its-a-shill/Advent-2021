# input_list = [l.rstrip('\n') for l in open("test_input.txt","r")]
input_list = [l.rstrip('\n') for l in open("input.txt", "r")]


dirs = [[0,1],[1,0],[0,-1],[-1,0]]

# Adds 10s on every edge of the map so I don't have to check if something's offscreen
map = [[10 for j in range(len(input_list[0])+2)] for i in range(len(input_list)+2)]
for i in range(len(input_list)):
    for j in range(len(input_list[0])):
        map[i+1][j+1] = int(input_list[i][j])

risk = 0
this_basin = [[(-2,-2) for i in range(len(map[0]))] for j in range(len(map))]
basins = {}

# For every point, checks if there's a direction where it doesn't increase
for i in range(1,len(map)-1):
    for j in range(1,len(map[i])-1):
        minpt = True
        for d in dirs:
            if map[i+d[0]][j+d[1]] <= map[i][j]:
                minpt = False
                break

        if minpt:
            risk += 1 + map[i][j]
            basins[(i,j)] = 1
            this_basin[i][j] = (i,j)

print('part 1')
print(risk)


# Finds what basin a given point is in
def find_basin(i,j):

    # Ignores if we already looked at this value
    if this_basin[i][j] != (-2,-2):
        return

    # Ignores if this is a peak
    if map[i][j] > 8:
        return

    # Ignores if this is already low point
    if (i,j) in basins:
        return

    # Finds a point the water could flow to
    nex = (-2, -2)
    for d in dirs:
        if map[i + d[0]][j + d[1]] < map[i][j]:
            nex = (i+d[0], j+d[1])
            break

    # For the point we flow to, find what basin that's in (recursively ofc)
    if nex != (-2, -2):
        if this_basin[nex[0]][nex[1]] == (-2, -2):
            find_basin(nex[0],nex[1])
        this_basin[i][j] = this_basin[nex[0]][nex[1]]
        basins[this_basin[i][j]] += 1

# Makes sure we check every point's basin at least once
for i in range(1,len(map)-1):
    for j in range(1,len(map[i])-1):
        find_basin(i,j)

sizes = sorted(basins.values())
print('part 2')
print(sizes[-1]*sizes[-2]*sizes[-3])
