import random
import heapq

# input_list = [l.rstrip('\n') for l in open("test_input.txt","r")]
input_list = [l.rstrip('\n') for l in open("input.txt", "r")]
input_list = [[int(x) for x in l] for l in input_list]

dirs = [[0,1],[1,0],[0,-1],[-1,0]]

def why_isnt_part_1_encoded_in_part_2(limits):

    # Acts as a priority queue
    boundary = [(0,0,0)]
    heapq.heapify(boundary)

    # Total distance to each point
    total_dist = [[10**12 for i in range(limits[0])] for j in range(limits[1])]
    total_dist[0][0] = 0

    # Finds the total distance to each point
    while len(boundary) > 0:
        curr = heapq.heappop(boundary)
        for d in dirs:

            # If the next point is in the search range, check if we need to put it in the boundary
            if 0 <= curr[1]+d[0] < len(total_dist) and 0 <= curr[2]+d[1] < len(total_dist[0]):
                nex = (curr[1]+d[0],curr[2]+d[1])

                # Figures out what the risk value of the next cell should be
                nex_val = input_list[nex[0] % len(input_list)][nex[1] % len(input_list[0])]
                nex_val += nex[0] // len(input_list) + nex[1] // len(input_list[0])
                nex_val = ((nex_val-1) % 9) + 1

                # If the next point can be found more cheaply than we thought, put it in the boundary
                if total_dist[nex[0]][nex[1]] > total_dist[curr[1]][curr[2]] + nex_val:
                    heapq.heappush(boundary,(total_dist[curr[1]][curr[2]] + nex_val,nex[0],nex[1]))
                    total_dist[nex[0]][nex[1]] = total_dist[curr[1]][curr[2]] + nex_val

    return total_dist[-1][-1]

# Why isn't part 1 encoded in part 2
print("Part 1")
print(why_isnt_part_1_encoded_in_part_2((len(input_list),len(input_list[0]))))

# Why isn't part 1 encoded in part 2
print("Part 2")
print(why_isnt_part_1_encoded_in_part_2((5*len(input_list),5*len(input_list[0]))))