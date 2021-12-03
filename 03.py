# input_list = [l.rstrip('\n') for l in open("test_input.txt","r")]
input_list = [l.rstrip('\n') for l in open("input.txt", "r")]

def values(inputs):
    vals = [0 for i in range(len(inputs[0]))]
    for line in inputs:
        for i in range(len(vals)):
            vals[i] += int(line[i])

    gamma = [2**(len(vals)-i-1) if vals[i] > len(inputs)/2 else 0 for i in range(len(vals))]
    gamma2 = [1 if vals[i] >= len(inputs)/2 else 0 for i in range(len(vals))]
    epsilon = [2**(len(vals)-i-1) if vals[i] < len(inputs)/2 else 0 for i in range(len(vals))]
    epsilon2 = [1 if vals[i] < len(inputs)/2 else 0 for i in range(len(vals))]
    return gamma,epsilon,gamma2,epsilon2

print('part 1')
print(sum(values(input_list)[0])*sum(values(input_list)[1]))

ox = 0
worked = input_list
for i in range(len(input_list[0])):
    gamma = values(worked)[2]
    next_list = []
    for line in worked:
        if int(line[i]) == gamma[i]:
            next_list.append(line)
    worked = next_list
    if len(worked) == 1:
        ox = int(worked[0],2)
        break

co2 = 0
worked = input_list
for i in range(len(input_list[0])):
    eps = values(worked)[3]
    next_list = []
    for line in worked:
        if int(line[i]) == eps[i]:
            next_list.append(line)
    worked = next_list
    if len(worked) == 1:
        co2 = int(worked[0],2)
        break

print('part 2')
print(ox*co2)