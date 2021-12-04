# input_list = [l.rstrip('\n') for l in open("test_input.txt","r")]
input_list = [l.rstrip('\n') for l in open("input.txt", "r")]

numbers = [int(x) for x in input_list[0].split(",")]

success = [[i,i+1,i+2,i+3,i+4] for i in range(0,25,5)]
success.extend([i,i+5,i+10,i+15,i+20] for i in range(5))

def find_data(board,numbers):
    board_hits = []
    for i in range(5,len(numbers)):
        for path in success:
            bingo = True
            for cell in path:
                if board[cell] not in numbers[:i]:
                    bingo = False
                    break
            if bingo:
                unchecked = 0
                for b in board:
                    if b not in numbers[:i]:
                        unchecked += b

                return i,unchecked*numbers[i-1]

i = 2
curr_board = []
best = [1000,0]
best_vals = [0, 0]
while i < len(input_list):
    if input_list[i] == "":
        curr,val = find_data(curr_board,numbers)
        if curr < best[0]:
            best[0] = curr
            best_vals[0] = val
        if curr > best[1]:
            best[1] = curr
            best_vals[1] = val
        curr_board = []
        i += 1
        continue
    curr_board.extend([int(x) for x in input_list[i].lstrip(" ").replace("  "," ").split(" ")])
    i += 1

print("Part 1")
print(best_vals[0])
print("Part 2")
print(best_vals[1])
