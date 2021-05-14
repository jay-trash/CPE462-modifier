import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import sys
import os

# choose which image to use mask on
# choose mask shape
# choose size (preferably more than 300 pixels)

#input = cv.imread(sys.argv[1])
#if input is None :
#    sys.exit("Could not read input")
#in_h, in_w, in_c = input.shape

#modif = cv.imread(sys.argv[2])
#if modif is None :
#    sys.exit("Could not read modifier")
#mod_h, mod_w, mod_c = modif.shape

print("You have chosen to put a mask on an image.")

#input and load images
debug = "false";
if len(sys.argv) != 4 or len(sys.argv) == 5 :
    if len(sys.argv) == 5 :
        if sys.argv[4] != "debug" :
            sys.exit("Pass 3 arguments, original image name(.jpg), modifier image name (.jpg), output name")
        elif sys.argv[4] == "debug":
            debug = "true"
    else :
        sys.exit("Pass 3 arguments, original image name(.jpg), modifier image name(.jpg), output name")

original = cv.imread(sys.argv[1])
if original is None :
    sys.exit("Could not read original input")
in_h, in_w, in_c = original.shape

modif = cv.imread(sys.argv[2])
if modif is None :
    sys.exit("Could not read modifier input")
mod_h, mod_w, mod_c = modif.shape

####


user_input = input("What shape do you want? [square] or [circle] ?")
if user_input == "square":
    
    img = cv.imread(sys.argv[1])
    cv.imshow('River', img)

    blank = np.zeros(img.shape[:2], dtype='uint8')
    #cv.imshow('Blank image', blank)

    mask = cv.rectangle(blank, (img.shape[1]//2 , img.shape[0]//2), (img.shape[1]//2 + 200, img.shape[0]//2 +200 ) ,255,-1)
    cv.imshow('Mask', mask)

    masked = cv.bitwise_and(img, img, mask=mask)
    cv.imshow('Masked image', masked)

    cv.waitKey(0)
elif user_input == "circle":

    img = cv.imread(sys.argv[1])
    cv.imshow('River', img)

    blank = np.zeros(img.shape[:2], dtype='uint8')
    #cv.imshow('Blank image', blank)

    mask = cv.circle(blank, (img.shape[1]//2 , img.shape[0]//2), 100,255,-1)
    cv.imshow('Mask', mask)

    masked = cv.bitwise_and(img, img, mask=mask)
    cv.imshow('Masked image', masked)

    cv.waitKey(0)



