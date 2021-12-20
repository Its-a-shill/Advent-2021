import numpy

# Help

# input_list = [l.rstrip('\n') for l in open("test_input.txt","r")]
input_list = [l.rstrip('\n') for l in open("input.txt", "r")]

frame = numpy.reshape(numpy.array(([2**i for i in range(8,-1,-1)])),(3,3))

algo = [1 if char == '#' else 0 for char in input_list[0]]

# I kinda why this amount of padding works
pad = 3*50

image = numpy.array([[1 if char == '#' else 0 for char in input_list[i]] for i in range(2,len(input_list))])
image = numpy.vstack((numpy.zeros((pad,len(image[0]))),image,numpy.zeros((pad,len(image[0])))))
image = numpy.hstack((numpy.zeros((len(image),pad)),image,numpy.zeros((len(image),pad))))

for count in range(50):
    new_img = numpy.zeros(image.shape)
    for i in range(1,len(image)-2):
        for j in range(1,len(image[0])-2):
            new_img[i][j] = algo[int(sum(sum(frame * image[i-1:i+2,j-1:j+2])))]
    # print(new_img)
    image = new_img

    if count == 1:
        extra = 2 * count

        pixel_ct = 0
        for row in image[pad - extra:-pad + extra]:
            for val in row[pad - extra:-pad + extra]:
                pixel_ct += val
        print('part 1')
        print(pixel_ct)


# This amount of padding is apparently not sensitive at all so i do not understand
extra = 2*count

pixel_ct = 0
for row in image[pad-extra:-pad+extra]:
    for val in row[pad-extra:-pad+extra]:
        pixel_ct += val
print('part 2')
print(pixel_ct)