import cv2
import numpy as np

# function that loads the bytes of an image
# input:    name of the file you want to load
# output:   a one-dimensional array of the integer repr. of the rgb
#               channels in an image file
# hint:     use opencv2
def load_image_bytes(file_name):
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
def decode_bytes(byte_list, num_bits, num_lsb=1):
    steg_bytes = []

    current_lsb = num_lsb - 1
    cover_idx = 0
    byte = ''
    for b in range(num_bits):
        byte += str((byte_list[cover_idx] & (1 << current_lsb)) >> current_lsb)
        if len(byte) == 8:
            steg_bytes.append(np.uint8(int(byte, 2)))
            byte = ''
        if current_lsb == 0:
            current_lsb = num_lsb - 1
            cover_idx += 1
        else:
            current_lsb -= 1
    return np.array(steg_bytes)


# function that takes in a list of "cover" bytes and "message" bits
#       and encodes those bits into the LSB of the cover bytes
# input:    byte list, bit list
# output:   byte list
def encode_bytes(cover_bytes, message_bits, num_lsb=1):
    lsb_bytes = cover_bytes.copy()

    current_lsb = num_lsb - 1
    cover_idx = 0
    for b in message_bits:
        lsb_bytes[cover_idx] = (lsb_bytes[cover_idx] & ~(1 << current_lsb)) | (b << current_lsb)

        if current_lsb == 0:
            current_lsb = num_lsb - 1
            cover_idx += 1
        else:
            current_lsb -= 1
    print("%d bits encoded." % len(message_bits))
    return lsb_bytes



if __name__=="__main__":
    choice = int(input("(1) Encode text in PNG\n(2) Decode text from PNG\n"))
    if choice == 1:
        png_filename =      input("PNG filename:\t\t\t")
        message_filename =  input("Message filename:\t\t")
        output_filename =   input("Output filename:\t\t")
        num_lsb_change =    eval(input("Number of LSBs to change:\t"))
        
        image_bytes, output_dim = load_image_bytes(png_filename)
        message_bytes = load_text_bytes(message_filename)
        message_bits = bits_from_bytes(message_bytes)

        if type(num_lsb_change) == int:
            lsb_bytes = encode_bytes(image_bytes, message_bits, num_lsb=num_lsb_change)
            save_image_bytes(output_filename, output_dim, lsb_bytes)
        else:
            start, stop = num_lsb_change
            for i in range(start, stop+1):
                lsb_bytes = encode_bytes(image_bytes, message_bits, num_lsb=i)
                save_image_bytes(output_filename[:-4] + str(i) + ".png", output_dim, lsb_bytes)
    if choice == 2:
        cover_fn = input("Cover filename:\t")
        message_out_fn = input("Message output filename:\t")
        num_bits_encoded = int(input("Number of encoded bits:\t"))
        num_lsb_decode =    int(input("Number of LSBs to decode:\t"))

        (cover_bytes, image_dim) = load_image_bytes(cover_fn)
        message_bytes = decode_bytes(cover_bytes, num_bits_encoded, num_lsb=num_lsb_decode)

        save_text_bytes(message_out_fn, message_bytes)
        
    
