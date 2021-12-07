# input_list = [l.rstrip('\n') for l in open("test_input.txt","r")]
input_list = [l.rstrip('\n') for l in open("input.txt", "r")]

vals = eval(input_list[0])

best = [1e12,1e12]
for loc in range(max(vals)):
    best[0] = min(best[0], sum(abs(v - loc) for v in vals))
    best[1] = min(best[1], sum((abs(v - loc)+1)*abs(v-loc)//2 for v in vals))

print("answers")
print(best)