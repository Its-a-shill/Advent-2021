# input_list = [l.rstrip('\n') for l in open("test_input.txt","r")]
input_list = [l.rstrip('\n') for l in open("input.txt", "r")]

inbits = bin(int(input_list[0],16))[2:]

# inbits += '0'*(4 - len(inbits)%4)
while len(inbits) % 4 != 0:
    inbits = '0'+inbits

data = {}

def decode(packet,depth=0):

    version = int(packet[:3],2)
    type = int(packet[3:6],2)

    # If type is 4, then process it as an integer
    if type == 4:
        outval = ''
        idx = 6
        while packet[idx] != '0':
            outval += packet[idx+1:idx+5]
            idx += 5
        outval += packet[idx + 1:idx + 5]
        idx += 5

        return version, idx, int(outval,2)

    # Why are there 2 different ways to specify
    len_id = packet[6] == '1'
    if len_id:
        sub_count = int(packet[7:7+11],2)
        sub_bits = -1
    else:
        sub_bits = int(int(packet[7:7+15],2))
        sub_count = -1

    idx = 7+(11 if len_id else 15)
    sub_counted = 0

    # Keeps track of both the version sum and the subpacket values
    tot_version = version
    values = []


    while idx - 22 != sub_bits and sub_count != sub_counted:

        # Does stuff with the subpackets
        sub_version,to_add,curr_val = decode(packet[idx:],depth=depth+1)
        values.append(curr_val)
        tot_version += sub_version
        idx += to_add
        sub_counted += 1

    # i didnt install 3.10 yet :(
    if type == 0:
        outval = sum(values)
    elif type == 1:
        outval = 1
        for v in values:
            outval *= v
    elif type == 2:
        outval = min(values)
    elif type == 3:
        outval = max(values)
    elif type == 5:
        outval = 1 if values[0] > values[1] else 0
    elif type == 6:
        outval = 1 if values[0] < values[1] else 0
    elif type == 7:
        outval = 1 if values[0] == values[1] else 0
    else:
        outval = -1

    return tot_version, idx, outval

p1,_,p2 = decode(inbits)
print('part 1')
print(p1)
print('part 2')
print(p2)