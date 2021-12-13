from matplotlib import pyplot as plt

# input_list = [l.rstrip('\n') for l in open("test_input.txt","r")]
input_list = [l.rstrip('\n') for l in open("input.txt", "r")]

pts = [eval(line) if "fold" not in line else None for line in input_list]

for line in input_list:
    newpts = set()
    if "fold" not in line:
        continue
    val = int(line.split("=")[1])
    for p in pts:
        if p == None:
            continue
        if 'y' in line:
            if p[1] > val:
                newpts.add((p[0],2*val - p[1]))
            else:
                newpts.add(p)
        else:
            if p[0] > val:
                newpts.add((2*val - p[0],p[1]))
            else:
                newpts.add(p)
    if None in pts:
        print('part 1')
        print(len(newpts))
        out = open("bleh.txt","w")
        for pt in newpts:
            out.write(str(pt)[1:-1]+'\n')
        out.close()
    pts = newpts

for pt in pts:
    plt.plot(pt[0],-pt[1],marker='.',ms=12)
plt.ylim(-16,2)
plt.title("part 2")
plt.show()