import numpy

# input_list = [l.rstrip('\n') for l in open("test_input.txt","r")]
input_list = [l.rstrip('\n') for l in open("input.txt", "r")]

move = {"forward":numpy.array([1,0]),"down":numpy.array([0,1]),"up":numpy.array([0,-1])}
aim = 0
position = [0,0]
for line in input_list:
    edit = (move[line.split(" ")[0]]*int(line.split(" ")[1]))
    position[0] += edit[0]
    position[1] += aim*edit[0]
    aim += edit[1]
print("part 1")
print(position[0]*aim)
print("part 2")
print(position[0]*position[1])


