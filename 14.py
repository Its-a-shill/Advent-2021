from matplotlib import  pyplot as plt

# input_list = [l.rstrip('\n') for l in open("test_input.txt","r")]
input_list = [l.rstrip('\n') for l in open("input.txt", "r")]

dirs = [[i//3 - 1,i%3 - 1] for i in range(9)]
dirs.remove([0,0])

all_letters = set()
rules = {}
base_polymer = {}

# Gets the first and last letter (which never change) so we can include them
bookends = (input_list[0][0], input_list[0][-1])

# Gets each polymerization rule,
# all of the pairs,
# and all of the possible letters
for i in range(2,len(input_list)):
    rules[input_list[i][:2]] = input_list[i][6]
    base_polymer[input_list[i][:2]] = 0
    all_letters |= set(input_list[i][:2])

# Encodes the initial polymer
polymer = base_polymer.copy()
for p in range(1,len(input_list[0])):
    polymer[input_list[0][p-1:p+1]] += 1


# Finds the difference between the max and min of the letters' representations
def find_diff(polymer):
    counts = {a:0 for a in all_letters}
    for pair in polymer:
        counts[pair[0]] += polymer[pair]
        counts[pair[1]] += polymer[pair]

    # Makes sure to count the start + end again
    for letter in bookends:
        counts[letter] += 1

    return max(counts.values())//2-min(counts.values())//2

diffs = [find_diff(polymer),]

# Inserts pairs
for i in range(40):

    # Does a polymerization
    nex = base_polymer.copy()
    for pair in rules:
        nex[pair[0] + rules[pair]] += polymer[pair]
        nex[rules[pair] + pair[1]] += polymer[pair]
    polymer = nex

    if i == 9:
        print('part 1')
        print(find_diff(polymer))

    diffs.append(find_diff(polymer))

print('part 2')
print(find_diff(polymer))

plt.plot([diffs[i]/diffs[i-1] for i in range(1,len(diffs))])
plt.show()