from collections import deque

# input_list = [l.rstrip('\n') for l in open("test_input.txt","r")]
input_list = [l.rstrip('\n') for l in open("input.txt", "r")]

def process(line):

    # Stores the list as as sequence of numbers and a string indicating structure
    # The numbers in the string don't matter, just there because it's easier to keep them
    seq = []
    for i,c in enumerate(line):
        if c in '0123456789':
            seq.append(int(c))

    changed = True
    while changed:
        nex_line = ""
        idx = 0
        depth = 0
        changed = False

        # Checks for the first number in an explode
        for i,c in enumerate(line):
            if depth > 4 and c in '0123456789':
                if 0 <= idx-1:
                    seq[idx-1] += seq[idx]
                if idx+2 <= len(seq)-1:
                    seq[idx+2] += seq[idx+1]
                del seq[idx]
                seq[idx] = 0

                # Assumes that anything in this nesting layer is a simple pair
                nex_line = line[:i-1] + "0" + line[i+4:]
                changed = True
                break

            if c == '[':
                depth += 1
            elif c == ']':
                depth -= 1
            elif c in '0123456789':
                idx += 1
                if idx == len(seq):
                    break

        # Checks for a number to split
        idx = 0
        depth = 0
        if not changed:
            for i, c in enumerate(line):
                if seq[idx] >= 10 and line[i] in '0123456789':
                    seq.insert(idx+1,(seq[idx]+1)//2)
                    seq[idx] = seq[idx]//2
                    changed = True
                    nex_line = line[:i] + "[0,0]" + line[i+1:]
                    break

                if c == '[':
                    depth += 1
                elif c == ']':
                    depth -= 1
                elif c in '0123456789':
                    idx += 1
                    if idx == len(seq):
                        break

        if changed:
            line = nex_line
    return rebuild(line, seq)

# From the structure and a sequence, makes the actual list this corresponds to
def rebuild(line,seq):
    idx = 0
    output = ""
    for c in line:
        if c in '0123456789':
            output += str(seq[idx])
            idx += 1
        else:
            output += c
    return output


def mag(line):
    if line in '0123456789':
        return int(line[0])

    depth = 0
    for i,c in enumerate(line):
        if depth == 1 and c==',':
            return 3*mag(line[1:i]) + 2*mag(line[i+1:-1])

        if c == '[':
            depth += 1
        elif c == ']':
            depth -= 1

# Part 1, sequentially adding each new line
curr = input_list[0]
curr = process(curr)
for line in input_list[1:]:
    curr = "[{0},{1}]".format(curr,line)
    curr = process(curr)
print('part 1')
print(mag(curr))

# Part 2, for each pair (in each direction) finds the max magnitude
best = 0
for i in range(len(input_list)):
    for j in range(i+1,len(input_list)):
        curr_mag = mag(process("[{0},{1}]".format(input_list[i],input_list[j])))
        best = max(best,curr_mag)

        curr_mag = mag(process("[{1},{0}]".format(input_list[i],input_list[j])))
        best = max(best,curr_mag)
print('part 2')
print(best)