# lis_in = [l.rstrip('\n') for l in open("test_input.txt","r")]
lis_in = [l.rstrip('\n') for l in open("input.txt","r")]

hits = 0
for i in range(3,len(lis_in)):
    if int(lis_in[i]) > int(lis_in[i-3]):
        hits += 1
print(hits)