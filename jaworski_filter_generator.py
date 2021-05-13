#Made by Matthew Jaworski
#I pledge my honor that I have abided by the Stevens Honor System.

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



red_channel = 0
green_channel = 0
blue_channel = 0

for x in range(0,final_h) :
    for y in range(0,final_w) :

        red_channel += modif.item(x,y,0)
        green_channel += modif.item(x,y,1)
        blue_channel += modif.item(x,y,2)


red_channel = int(red_channel)
green_channel = int(green_channel)
blue_channel = int(blue_channel)

total_pixels = final_h * final_w

red_avg = red_channel/total_pixels
green_avg = green_channel/total_pixels
blue_avg = blue_channel/total_pixels


#RED CHANNEL
if red_avg >= 0 and red_avg <=84:

    for x in range(0,final_h) :
        for y in range(0,final_w) :
            if input.item(x,y,0) >= 85:
                input.itemset((x,y,0),84)

elif red_avg >= 85 and red_avg <=170:

    for x in range(0,final_h) :
        for y in range(0,final_w) :
            if input.item(x,y,0) <= 84:
                input.itemset((x,y,0),85)
            elif input.item(x,y,0) >= 170:
                input.itemset((x,y,0),171)

elif red_avg >= 171 and red_avg <=255:

    for x in range(0,final_h) :
        for y in range(0,final_w) :
            if input.item(x,y,0) <= 170:
                input.itemset((x,y,0),171)



#GREEN CHANNEL
if green_avg >= 0 and green_avg <=84:

    for x in range(0,final_h) :
        for y in range(0,final_w) :
            if input.item(x,y,1) >= 85:
                input.itemset((x,y,1),84)

elif green_avg >= 85 and green_avg <=170:

    for x in range(0,final_h) :
        for y in range(0,final_w) :
            if input.item(x,y,1) <= 84:
                input.itemset((x,y,1),85)
            elif input.item(x,y,1) >= 170:
                input.itemset((x,y,1),171)

elif green_avg >= 171 and green_avg <=255:

    for x in range(0,final_h) :
        for y in range(0,final_w) :
            if input.item(x,y,1) <= 170:
                input.itemset((x,y,1),171)



#BLUE CHANNEL
if blue_avg >= 0 and blue_avg <=84:

    for x in range(0,final_h) :
        for y in range(0,final_w) :
            if input.item(x,y,2) >= 85:
                input.itemset((x,y,2),84)

elif blue_avg >= 85 and blue_avg <=170:

    for x in range(0,final_h) :
        for y in range(0,final_w) :
            if input.item(x,y,2) <= 84:
                input.itemset((x,y,2),85)
            elif input.item(x,y,2) >= 170:
                input.itemset((x,y,2),171)

elif blue_avg >= 171 and blue_avg <=255:

    for x in range(0,final_h) :
        for y in range(0,final_w) :
            if input.item(x,y,2) <= 170:
                input.itemset((x,y,2),171)


#cv.imwrite(sys.argv[3], input)
cv.imshow(sys.argv[3], input)
cv.waitKey(0)