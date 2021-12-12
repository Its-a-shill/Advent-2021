# input_list = [l.rstrip('\n') for l in open("test_input.txt","r")]
input_list = [l.rstrip('\n') for l in open("input.txt", "r")]

# Puts input into the adjacency lookup table
paths = {}
for line in input_list:
    pts = line.split('-')
    for i in range(2):
        if pts[i] not in paths:
            paths[pts[i]] = []
        paths[pts[i]].append(pts[1-i])

# Give it an initial path and it'll recursively find all valid paths that continue it
def add_path(curr_paths, part2 = False, doubled = False):
    global total_count

    # If we've hit the end we're done
    curr_node = curr_paths[-1]
    if curr_node == 'end':
        total_count += 1
        return

    # Checks everything this cave connects to, if we can visit then try it
    for next_node in paths[curr_node]:

        # Part 2 allows one lowercase cave to be visited twice
        if part2:
            if (not next_node.isupper() and curr_paths.count(next_node)>=1 and doubled) or (next_node=='start'):
                continue
            add_path(curr_paths + [next_node], part2, doubled or (not next_node.isupper() and curr_paths.count(next_node)>=1))

        # Part 1 requires all lowercase caves to be visited at most once
        else:
            if (not next_node.isupper()) and curr_paths.count(next_node)>=1:
                continue
            add_path(curr_paths + [next_node])

total_count = 0
add_path(['start'])
print('part 1')
print(total_count)

total_count = 0
print('part 2')
add_path(['start'],True)
print(total_count)