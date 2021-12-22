# input_list = [l.rstrip('\n') for l in open("test_input.txt","r")]
input_list = [l.rstrip('\n') for l in open("input.txt", "r")]

count = 0

switches = []
bds = []
for line in input_list:
    thing = line.replace(".","=").replace(",","=").split("=")
    bds.append([[int(thing[1]),int(thing[3])],[int(thing[5]),int(thing[7])],[int(thing[9]),int(thing[11])]])
    switches.append(line[1]=='n')

# Checks whether there is overlap between inputs
def pair_overlap(regions):
    for i in range(3):
        if not (regions[0][i][0] <= regions[1][i][1] and regions[1][i][0] <= regions[0][i][1]):
            return False

    return True

# Assuming there is overlap, find the region of overlap
def vol_overlap(regions):
    pair_bd = []
    for i in range(3):
        pair_bd.append([max(regions[0][i][0],regions[1][i][0]),min(regions[0][i][1],regions[1][i][1])])
    return pair_bd

# Given a region, find its volume
def vol(region):
    prod = 1
    for i in range(3):
        prod *= 1+region[i][1] - region[i][0]
    return prod

# Adds a new region to the current,
#  replacing its function with regions that are either entirely on or entirely off
#  so that intersection effects are canceled
def process(curr_bds,curr_switches,nex,nex_switch,part1 = False):
    out_bds = curr_bds.copy()
    out_switches = curr_switches.copy()

    for i,bd in enumerate(curr_bds):
        if pair_overlap((bd,nex)):
            overlap = vol_overlap((bd,nex))
            if curr_switches[i]:
                out_bds.append(overlap)
                out_switches.append(False)
            else:
                out_bds.append(overlap)
                out_switches.append(True)

    if nex_switch:
        out_bds.append(nex)
        out_switches.append(True)

    return out_bds,out_switches

# Builds up a new set where every action either has everything inside it on or everything off before it acts
#  this set is very easy to find the total volume of
def evaluate(cover):
    updated_bds = []
    updated_switches = []
    for i in range(len(bds)):
        if pair_overlap((bds[i], cover)):
            updated_bds, updated_switches = process(updated_bds, updated_switches, vol_overlap((bds[i], cover)),
                                                    switches[i])

    count = 0
    for i in range(len(updated_switches)):
        count += vol(updated_bds[i]) * (1 if updated_switches[i] else -1)
    return count

# Part 1 limits the search area to [-50,50] in all axes
cover_1 = [[-50,50]]*3
print('part 1')
print(evaluate(cover_1))

# Part 2 has no direct limits on search area, so this should be fine
cover_2 = [[-10**20,10**20]]*3
print('part 2')
print(evaluate(cover_2))