# input_list = [l.rstrip('\n') for l in open("test_input.txt","r")]
input_list = [l.rstrip('\n') for l in open("input.txt", "r")]

import itertools

# Part 1 was ezpz if I could learn how to read
known_sizes = {2, 3, 4, 7}
count = 0
for line in input_list:
    line_set = set()
    for s in line.split(" | ")[1].split(" "):
        if(len(s)) in known_sizes:
            count += 1
print('part 1')
print(count)


letters = ['a','b','c','d','e','f','g']
lett2 = {letters[k]:k for k in range(7)}
possible = [{0,1,2,4,5,6},{2,5},{0,2,3,4,6},{0,2,3,5,6},{1,2,3,5},{0,1,3,5,6},{0,1,3,4,5,6},{0,2,5},{0,1,2,3,4,5,6},{0,1,2,3,5,6}]
sumvals = 0

for line in input_list:

    # Just putting this here instead of inline later so it's a bit cleaner
    words = line.split(" | ")[0].split(" ")

    # Check every possible permutation and see if it could have resulted in this matching
    for map in itertools.permutations(range(7)):

        # I'm sure there's a pythonic version of this construct but i dont know it
        worked = True
        for word in words:
            if set(map[lett2[l]] for l in word) not in possible:
                worked = False
                break
        if worked:

            # Yeah I could've put this after the break and that would've looked nicer possibly
            # Also surely theres a way to cast a generator to a string properly but i dont know it
            s = ""
            for word in line.split(" | ")[1].split(" "):
                s += str(possible.index(set(map[lett2[l]] for l in word)))
            sumvals += int(s)
            break

print('part 2')
print(sumvals)