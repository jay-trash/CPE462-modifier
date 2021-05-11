import cv2 as cv
import numpy as np
import sys


debug = "false";
if len(sys.argv) != 4 or len(sys.argv) == 5 :
    if len(sys.argv) == 5 :
        if sys.argv[4] != "debug" :
            sys.exit("Pass 3 arguments, input image name, modifier image name, output name")
        elif sys.argv[4] == "debug":
            debug = "true"
    else :
        sys.exit("Pass 3 arguments, input image name, modifier image name, output name")

input = cv.imread(sys.argv[1])
if input is None :
    sys.exit("Could not read input")
in_h, in_w, in_c = input.shape

modif = cv.imread(sys.argv[2])
if modif is None :
    sys.exit("Could not read modifier")
mod_h, mod_w, mod_c = modif.shape






#resize images to same res

if debug == "true" :
    print("Initial resolution input: " + str(in_w) + " by " + str(in_h))
    print("Initial resolution modif: " + str(mod_w) + " by " + str(mod_h))

if in_h > mod_h and in_w > mod_w :
    input = cv.resize(input, (mod_w, mod_h))
    final_w = mod_w
    final_h = mod_h
elif mod_h > in_h and mod_w > in_w :
    modif = cv.resize(modif, (in_w, in_h))
    final_w = in_w
    final_h = in_h
else :
    if in_h < mod_h :
        cram_h = in_h
    else :
        cram_h = mod_h
    if in_w < mod_w :
        cram_w = in_w
    else :
        cram_w = mod_w
    input = cv.resize(input, (cram_w, cram_h))
    modif = cv.resize(modif, (cram_w, cram_h))
    final_w = cram_w
    final_h = cram_h

if debug == "true" :
    print("Final resolution: " + str(final_w) + " by " + str(final_h))
    cv.imshow("Raw Input", input)
    cv.waitKey(0)

#to run these, use the same image twice
'''for x in range(0,final_h) :
    for y in range(0,final_w) :
        #get sums of each color channel
        input.itemset((x,y,0),modif.item(x,y,2))
        input.itemset((x,y,1),modif.item(x,y,0))
        input.itemset((x,y,2),modif.item(x,y,1))'''

'''for x in range(0,final_h) :
    for y in range(0,final_w) :
        #get sums of each color channel
        input.itemset((x,y,0),modif.item(x,y,1))
        input.itemset((x,y,1),modif.item(x,y,2))
        input.itemset((x,y,2),modif.item(x,y,0))'''

#this is the contrast one
#commented out stuff in the contrast code is the "Color Weirder"
for x in range(0,final_h) :
    for y in range(0,final_w) :
        '''num1 = modif.item(x,y,0)
        num2 = modif.item(x,y,1)
        num3 = modif.item(x,y,2)'''

        num1 = input.item(x,y,0)
        num2 = input.item(x,y,1)
        num3 = input.item(x,y,2)


        dist1 = 255 - num1
        dist2 = 255 - num2
        dist3 = 255 - num3

        if dist1 >= num1:
            input.itemset((x,y,0),0)
        else:
            input.itemset((x,y,0),255)

        if dist2 >= num2:
            input.itemset((x,y,1),0)
        else:
            input.itemset((x,y,1),255)

        if dist3 >= num3:
            input.itemset((x,y,2),0)
        else:
            input.itemset((x,y,2),255)
        '''num4 = input.item(x,y,0)
        num5 = input.item(x,y,1)
        num6 = input.item(x,y,2)

        if num1 >= num2 and num2 >= num3:
            input.itemset((x,y,0),num4)
            input.itemset((x,y,1),num5)
            input.itemset((x,y,2),num6)
        elif num1 >= num3 and num3 >= num2:
            input.itemset((x,y,0),num4)
            input.itemset((x,y,1),num6)
            input.itemset((x,y,2),num5)
        elif num2 >= num1 and num1 >= num3:
            input.itemset((x,y,0),num5)
            input.itemset((x,y,1),num4)
            input.itemset((x,y,2),num6)
        elif num2 >= num3 and num3 >= num1:
            input.itemset((x,y,0),num5)
            input.itemset((x,y,1),num6)
            input.itemset((x,y,2),num4)
        elif num3 >= num1 and num1 >= num2:
            input.itemset((x,y,0),num6)
            input.itemset((x,y,1),num4)
            input.itemset((x,y,2),num5)
        elif num3 >= num2 and num2 >= num1:
            input.itemset((x,y,0),num6)
            input.itemset((x,y,1),num5)
            input.itemset((x,y,2),num4)'''

cv.imshow(sys.argv[3], input)
cv.waitKey(0)