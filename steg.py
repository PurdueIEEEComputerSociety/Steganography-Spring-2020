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
# input:    probably an output name and the bytes
# output:   nothing, just saves the image


# function that loads a .txt file and returns its bytes
# input:    file name
# output:   a one-dimensional array of the integer repr. of the file's bytes
#
# hint:     look up opening files in python?

