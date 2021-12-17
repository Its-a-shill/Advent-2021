import math

# bds = [20,30,-10,-5]
bds = [188,221,-122,-74]

# Gets the min and max values of initial x vel that land in the box after T timesteps
def x(bds,T):

    # Use a base formula
    min_x0 = math.ceil((2*bds[0] + T**2 - T)/(2*T))
    max_x0 = math.floor((2*bds[1] + T**2 - T)/(2*T))

    # If the base formula needed a negative x vel, use a different formula that's just for nonnegatives
    if min_x0 < T:
        min_x0 = math.ceil((2*bds[0]-1/4)**0.5-1/2)

    if max_x0 < T:
        max_x0 = math.floor((2*bds[1]-1/4)**0.5-1/2)

    return min_x0,max_x0

# Gets the min and max values of initial y vel that land in the box after T timesteps
def y(bds,T):

    # y velocity can be negative so we don't need to worry about the same thing as x
    min_y0 = math.ceil((2*bds[2] + T**2 - T)/(2*T))
    max_y0 = math.floor((2*bds[3] + T**2 - T)/(2*T))

    return min_y0,max_y0

# Turns out this just gives you the y velocity for part 1 haha i hate physics and reading
print('part 1 (highest without considering x)')
print((-bds[2]-1)*(-bds[2])//2)

# Goes through each pair of things that works
#  I want to be able to count it more directly, but some trajectories end in the box twice or more
#  and the inclusion/exclusion for that sounds much more annoying
hits = set()
highest = 0
for t in range(1,-2*bds[2]+2):
    x_range = x(bds,t)
    y_range = y(bds,t)
    for xi in range(x_range[0],x_range[1]+1):
        for yi in range(y_range[0],y_range[1]+1):
            highest = max(highest,(y_range[1]*(y_range[1]+1))//2)

            hits.add((xi,yi))

print('\npart 1 (highest with considering x - eric doesn\'t hate us *that* much so it should be the same)')
print(highest)

print('\npart 2')
print(len(hits))