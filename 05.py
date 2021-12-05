from math import *
from numpy import sign

# input_list = [l.rstrip('\n') for l in open("test_input.txt","r")]
input_list = [l.rstrip('\n') for l in open("input.txt", "r")]

lines = []
for line in input_list:
    lines.append([eval(line.split(" -> ")[0]),eval(line.split(" -> ")[1])])

hits_1 = {}
hits_2 = {}

for line in lines:
    xslope = (line[1][0] - line[0][0])
    yslope = (line[1][1] - line[0][1])
    for i in range(max(abs(xslope),abs(yslope))+1):
        hit = (line[0][0] + sign(xslope) * i, line[0][1] + sign(yslope) * i)

        if xslope*yslope == 0:
            if hit in hits_1:
                hits_1[hit] += 1
            else:
                hits_1[hit] = 1

        if hit in hits_2:
            hits_2[hit] += 1
        else:
            hits_2[hit] = 1

num_1 = 0
for pt in hits_1:
    if hits_1[pt] >= 2:
        num_1 += 1

print('part 1',num_1,sep='\n')

num_2 = 0
for pt in hits_2:
    if hits_2[pt] >= 2:
        num_2 += 1

print('part 2',num_2,sep='\n')