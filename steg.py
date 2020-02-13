import cv2

# function that loads the bytes of an image
# input:    name of the file you want to load
# output:   a one-dimensional array of the integer repr. of the rgb
#               channels in an image file
# hint:     use opencv2
def  load_image_bytes(file_name):
    image_bytes = cv2.imread(file_name, cv2.IMREAD_COLOR)
    return image_bytes.flatten()

# function that saves the bytes of an image
# input:    probably an output name and the bytes (where bytes are
#                               probably a flattened numpy array)
# output:   nothing, just saves the image
def save_image_bytes(file_name, image_dim, image_bytes):
    pixels = image_bytes.reshape((image_dim[0], image_dim[1], 3))
    cv2.imwrite(file_name, pixels)



# function that loads a .txt file and returns its bytes
# input:    file name
# output:   a one-dimensional array of the integer repr. of the file's bytes
#
# hint:     look up opening files in python?
def load_text_bytes(file_name):
    with open(file_name, 'rb') as f:
        text_bytes = f.read()
    return text_bytes


# function that takes in a list of bytes and returns a list where each
#       element is a bit
# input:    byte list
# output:   bit list
def bits_from_bytes(byte_list):
    bits = [int(bit)  for byte in byte_list for bit in bin(byte)[2:].zfill(8)]
    return bits




# function that takes in a list of "cover" bytes and "message" bits
#       and encodes those bits into the LSB of the cover bytes
# input:    byte list, bit list
# output:   byte list
























