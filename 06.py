# input_list = [l.rstrip('\n') for l in open("test_input.txt","r")]
input_list = [l.rstrip('\n') for l in open("input.txt", "r")]

fish = [0 for i in range(9)]

for v in input_list[0].split(','):
    fish[int(v)] += 1

for day in range(256):
    nex = [0 for i in range(9)]
    nex[0] = fish[1]
    nex[1] = fish[2]
    nex[2] = fish[3]
    nex[3] = fish[4]
    nex[4] = fish[5]
    nex[5] = fish[6]
    nex[6] = fish[7] + fish[0]
    nex[7] = fish[8]
    nex[8] = fish[0]
    fish = nex

    if day == 79:
        print('part 1')
        print(sum(fish))

print('part 2')
print(sum(fish))