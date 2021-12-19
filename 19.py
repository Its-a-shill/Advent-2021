import numpy

# input_list = [l.rstrip('\n') for l in open("test_input.txt","r")]
input_list = [l.rstrip('\n') for l in open("input.txt", "r")]

# Gets all the positive/negative axis values
transforms = [numpy.diag([1 if i&2**j != 0 else -1 for j in range(3)]) for i in range(8)]

# Swaps 2 axes
swap = numpy.array(((1,0,0),
                   (0,0,1),
                   (0,1,0)))
# Rotates all 3 axes
rot = numpy.array(((0,1,0),
                   (0,0,1),
                   (1,0,0)))

# Does both operations as many times as necessary
for t in transforms.copy():
    transforms.append(swap @ t)
for t in transforms.copy():
    if any((rot @ t == x).all() for x in transforms):
        print(rot @ t)
    else:
        transforms.append(rot @ t)
    if any((rot @ rot @ t == x).all() for x in transforms):
        print(rot @ rot @ t)
    else:
        transforms.append(rot @ rot @ t)

# There are 48?? The description says 24 but I can't figure out a way to make that work

# Gets input, separated by each scan
scanner_pts = []
for line in input_list:
    if "scanner" in line:
        scanner_pts.append([])
    elif ',' in line:
        scanner_pts[-1].append([int(x) for x in line.split(',')])

# Sorts and absolute values the differences between two pts from the same scan
#  The result of this operation is independent of scanner position or orientation
#  This seems kinda superfluous, but it's faster than doing the whole overlap check i think
def abs_diffs(scan, pt):
    diff_set = set()
    for s in scan:
        diff_set.add(tuple(sorted([abs(s[i]-pt[i]) for i in range(3)])))
    return diff_set

# Just gets the differences between two pts from the same scan
def diffs(scan,pt):
    diff_list = []
    for s in scan:
        diff_list.append(tuple([s[i]-pt[i] for i in range(3)]))
    return diff_list

# Checks if two differences represent the same pair of beacons
def abs_eq(scan0,scan1):
    return set([abs(s) for s in scan0]) == set([abs(s) for s in scan1])

# Finds which differences specifically we're talking about that are the same pair
def find_overlap(signed0,signed1):
    overlap = []
    for i in range(len(signed0)):
        for j in range(len(signed1)):
            if abs_eq(signed0[i],signed1[j]):
                overlap.append([i,j,signed0[i],signed1[j]])
    return overlap

# Keeps track of locations and orientations of each scanner
locs = [numpy.zeros(3) for i in range(len(scanner_pts))]
scan_transforms = [numpy.eye(3) for i in range(len(scanner_pts))]

# We define our coordinate system by the scanner 0
#  That in mind, this list keeps track of which scanners we know
found = [0]

# Basically given a pair of scanners, this checks if they overlap 12 beacons
#  And if they do, finds the position/orientation of the 2nd in terms of the 1st
#  Side effects are good prove me wrong
def find_loc(i,j):
    flag = False
    for center0 in scanner_pts[i]:
        set0 = abs_diffs(scanner_pts[i], center0)
        for center1 in scanner_pts[j]:
            set1 = abs_diffs(scanner_pts[j], center1)
            if len(set0 & set1) >= 12:
                overlap = find_overlap(diffs(scanner_pts[i],center0), diffs(scanner_pts[j], center1))
                for t in transforms:
                    worked = True
                    for o in overlap[1:]:
                        if numpy.linalg.norm(numpy.array(o[2]) - t @ o[3]) > 1:
                            worked = False
                    if worked:
                        scan_transforms[j] = t.copy()
                        break
                try:

                    rel_loc = - (scan_transforms[j] @ scanner_pts[j][overlap[0][1]] - numpy.array(scanner_pts[i][overlap[0][0]]))
                    abs_loc = (scan_transforms[i] @ rel_loc) + locs[i]
                    locs[j] = abs_loc
                    # print(rel_loc)
                    # print((scan_transforms[i] @ rel_loc))
                    # print(abs_loc)
                    scan_transforms[j] = scan_transforms[i] @ scan_transforms[j]
                    found.append(j)
                    flag = True
                    return True
                except:
                    for o in overlap:
                        print(o)
    return False

# Goes through every pair of scanners until we know all the scanners or can't find any more info
#  Turns out python iterables work exactly as I need them to
for i in found:
    for j in range(len(scanner_pts)):
        # print(i,j)
        if j not in found:
            success = find_loc(i,j)
            # print(i,j,success)

# Does part 1, by adding all of the beacon pts to a set and counting how many are unique
total_pts = set()
for i,s in enumerate(scanner_pts):
    for pt in s:
        total_pts.add(tuple(locs[i] + scan_transforms[i] @ pt))
print('part 1')
print(len(total_pts))

# Does part 2, by finding the manhattan distance between every pair
max_dist = 0
for t1 in locs:
    for t2 in locs:
        max_dist = max(max_dist,sum(abs(t1[i]-t2[i]) for i in range(3)))
print('part 2')
print(max_dist)