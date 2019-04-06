# Preprocessing the image to match the MNIST format for more accuracy
# Inspiration and code from 
# http://opensourc.es/blog/tensorflow-mnist

import numpy as np
import cv2
import math
from scipy import ndimage
import sys

def getBestShift(img):
    cy,cx = ndimage.measurements.center_of_mass(img)

    rows,cols = img.shape
    shiftx = np.round(cols/2.0-cx).astype(int)
    shifty = np.round(rows/2.0-cy).astype(int)

    return shiftx,shifty


def shift(img,sx,sy):
    rows,cols = img.shape
    M = np.float32([[1,0,sx],[0,1,sy]])
    shifted = cv2.warpAffine(img,M,(cols,rows))
    return shifted

def process_image(image_path, filename, output_directory):
        # Read image as grayscale
        gray_image = cv2.imread(image_path + filename, 0)

	# Invert image (black background) and set size to 28, 28
        gray_image = cv2.resize(255-gray_image, (28, 28))

	# better black and white version
        (thresh, gray_image) = cv2.threshold(gray_image, 128, 255, 					cv2.THRESH_BINARY | cv2.THRESH_OTSU)

        while np.sum(gray_image[0]) == 0:
            gray_image = gray_image[1:]

        while np.sum(gray_image[:,0]) == 0:
            gray_image = np.delete(gray_image,0,1)

        while np.sum(gray_image[-1]) == 0:
            gray_image = gray_image[:-1]

        while np.sum(gray_image[:,-1]) == 0:
            gray_image = np.delete(gray_image, -1, 1)

        # MNIST defines that the number must fit inside 20px
        # The rest 8 pixels are black
        rows,cols = gray_image.shape

        if rows > cols:
            factor = 20.0 / rows
            rows = 20
            cols = int(round(cols * factor))
            # First cols than rows
            gray_image = cv2.resize(gray_image, (cols, rows))
        else:
            factor = 20.0 / cols
            cols = 20
            rows = int(round(rows*factor))
            # First cols than rows
            gray_image = cv2.resize(gray_image, (cols, rows))

        colsPadding = (int(math.ceil((28-cols)/2.0)),
                        int(math.floor((28-cols)/2.0)))
        rowsPadding = (int(math.ceil((28-rows)/2.0)),
                        int(math.floor((28-rows)/2.0)))
        gray_image = np.lib.pad(gray_image, (rowsPadding,
                                        colsPadding), 'constant')

        shiftx,shifty = getBestShift(gray_image)
        shifted = shift(gray_image ,shiftx, shifty)
        gray_image = shifted

        # save the processed images
        output = output_directory + filename
        cv2.imwrite(output, gray_image)
        return output
