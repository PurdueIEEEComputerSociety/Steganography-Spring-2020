import cv2
import numpy as np

# function that loads the bytes of an image
# input:    name of the file you want to load
# output:   a one-dimensional array of the integer repr. of the rgb
#               channels in an image file
# hint:     use opencv2
def  load_image_bytes(file_name):
    image_bytes = cv2.imread(file_name, cv2.IMREAD_COLOR)
    return (image_bytes.flatten(), image_bytes.shape)


# function that saves the bytes of an image
# input:    probably an output name and the bytes (where bytes are
#                               probably a flattened numpy array)
# output:   nothing, just saves the image
def save_image_bytes(file_name, image_dim, image_bytes):
    pixels = image_bytes.reshape(image_dim)
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


def save_text_bytes(file_name, file_bytes):
    with open(file_name, 'wb') as f:
        f.write(file_bytes)


# function that takes in a list of bytes and returns a list where each
#       element is a bit
# input:    byte list
# output:   bit list
def bits_from_bytes(byte_list):
    bits = [int(bit)  for byte in byte_list for bit in bin(byte)[2:].zfill(8)]
    return bits

# function that takes in a list of bytes and returns encoded data
#       in those bytes
# input:    byte list, number of bits encoded
# output:   byte list (LSBs from cove file)
def get_steg_bytes(byte_list, num_bits):
    steg_bytes = []
    byte = ''
    for b in range(num_bits):
        byte += str(byte_list[b] & 1)
        if len(byte) == 8:
            steg_bytes.append(np.uint8(int('{:<08s}'.format(byte), 2)))
            byte = ''
    return np.array(steg_bytes)


# function that takes in a list of "cover" bytes and "message" bits
#       and encodes those bits into the LSB of the cover bytes
# input:    byte list, bit list
# output:   byte list
def get_lsb_bytes(cover_bytes, message_bits):
    lsb_bytes = cover_bytes.copy()
    for idx, b in enumerate(message_bits):
        lsb_bytes[idx] = (lsb_bytes[idx] & ~1) | b
    return lsb_bytes

if __name__=="__main__":

    cover_fn = "output.png"
    message_out_fn = "message2.txt"

    (cover_bytes,_) = load_image_bytes(cover_fn)
    message_bytes = get_steg_bytes(cover_bytes, 998592)

    save_text_bytes(message_out_fn, message_bytes)

    #image_fn = "donut.png"
    #message_fn = "message.txt"
    #output_fn = "output.png"

    #image_bytes, output_dim = load_image_bytes(image_fn)
    #message_bytes = load_text_bytes(message_fn)
    #message_bits = bits_from_bytes(message_bytes)

    #lsb_bytes = get_lsb_bytes(image_bytes, message_bits)

    #save_image_bytes(output_fn, output_dim, lsb_bytes)
