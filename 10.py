# input_list = [l.rstrip('\n') for l in open("test_input.txt","r")]
input_list = [l.rstrip('\n') for l in open("input.txt", "r")]

cost = {')':3,']':57,'}':1197,'>':25137}
starts = '([{<'
ends = ')]}>'
ending = {'(':')','[':']','{':'}','<':'>'}
chars = ['()','[]','{}','<>']

total1 = 0
total2 = []

points = {')':1,']':2,'}':3,'>':4}

def check_corrupted(line):
    for i in range(len(line)):
        for c in chars:
            line = line.replace(c,'')

    for i in range(len(line)-1):
        if line[i] in starts and line[i+1] in ends and line[i+1] != ending[line[i]]:
            return cost[line[i+1]]
    return 0

def eval_incomplete(line):
    stack = []
    for s in line:
        if s in starts:
            stack.append(s)
        elif s == ending[stack[-1]]:
            stack = stack[:-1]
    score = 0
    for x in stack[::-1]:
        score *= 5
        score += points[ending[x]]
    return score

for line in input_list:
    corrupted = check_corrupted(line[:])
    total1 += corrupted

    if corrupted == 0:
        total2.append(eval_incomplete(line))

print('part 1')
print(total1)
print('part 2')
print(sorted(total2)[len(total2)//2])