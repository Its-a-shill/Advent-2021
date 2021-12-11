# input_list = [l.rstrip('\n') for l in open("test_input.txt","r")]
input_list = [l.rstrip('\n') for l in open("input.txt", "r")]

# Processes input as ints
grid = [[int(x) for x in line] for line in input_list]

# Gets all adjacent points with minimal energy
dirs = [[i//3 - 1,i%3 - 1] for i in range(9)]
dirs.remove([0,0])

# Why am i initializing these here
count_flashes = 0
flashed = set()

# Does a flash
def flash(i,j):
    global count_flashes

    # Keeps track of who's flashed so far this round
    if (i,j) in flashed:
        return
    flashed.add((i,j))
    count_flashes += 1

    # Tells everyone around the flasher to increment
    for dir in dirs:
        if 0 <= i+dir[0] < len(grid) and 0 <= j+dir[1] < len(grid[0]):
            grid[i+dir[0]][j+dir[1]] += 1
            if grid[i+dir[0]][j+dir[1]] > 9:
                flash(i+dir[0],j+dir[1])
    return


for timestep in range(10**5):
    flashed = set()

    # Flashes
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j] += 1
            if grid[i][j] > 9:
                flash(i,j)

    # Unflashes
    for pt in flashed:
        grid[pt[0]][pt[1]] = 0

    if timestep == 100:
        print('part 1')
        print(count_flashes)

    # Tells part 2 to happen
    if(len(flashed) == len(grid)*len(grid[0])):
        print('part 2')
        print(timestep+1)
        break