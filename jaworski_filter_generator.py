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

#take modifier image
#take average of reds, greens, and blues
#classify those averages as low, medium, or high
#red change
    #if seed low
        #already in range kept same
        #greater than changed to 84
    #if seed medium
        #already in range kept same
        #less than changed to 85
        #greater than changed to 170
    #if seed high
        #already in range kept same
        #less than changed to 171
#green change
    #if seed low
        #already in range kept same
        #greater than changed to 84
    #if seed medium
        #already in range kept same
        #less than changed to 85
        #greater than changed to 170
    #if seed high
        #already in range kept same
        #less than changed to 171
#blue change
    #if seed low
        #already in range kept same
        #greater than changed to 84
    #if seed medium
        #already in range kept same
        #less than changed to 85
        #greater than changed to 170
    #if seed high
        #already in range kept same
        #less than changed to 171
red_channel = 0
green_channel = 0
blue_channel = 0

#loop through the image's pixels
for x in range(0,final_h) :
    for y in range(0,final_w) :
        #get sums of each color channel
        red_channel += modif.item(x,y,0)
        green_channel += modif.item(x,y,1)
        blue_channel += modif.item(x,y,2)

#sum_inp1 = sum_inp1/3
#sum_inp2 = sum_inp2/3
#sum_inp3 = sum_inp3/3
red_channel = int(red_channel)
green_channel = int(green_channel)
blue_channel = int(blue_channel)

total_pixels = final_h * final_w

red_avg = red_channel/total_pixels
green_avg = green_channel/total_pixels
blue_avg = blue_channel/total_pixels

#red channel classifier modifier image
r_classifier = 0
g_classifier = 0
b_classifier = 0


#RED CHANNEL
if red_avg >= 0 and red_avg <=84:
    r_classifier = 0
    for x in range(0,final_h) :
        for y in range(0,final_w) :
            if input.item(x,y,0) >= 85:
                input.itemset((x,y,0),84)

elif red_avg >= 85 and red_avg <=170:
    r_classifier = 1
    for x in range(0,final_h) :
        for y in range(0,final_w) :
            if input.item(x,y,0) <= 84:
                input.itemset((x,y,0),85)
            elif input.item(x,y,0) >= 170:
                input.itemset((x,y,0),171)

elif red_avg >= 171 and red_avg <=255:
    r_classifier = 2
    for x in range(0,final_h) :
        for y in range(0,final_w) :
            if input.item(x,y,0) <= 170:
                input.itemset((x,y,0),171)



#GREEN CHANNEL
if green_avg >= 0 and green_avg <=84:
    g_classifier = 0
    for x in range(0,final_h) :
        for y in range(0,final_w) :
            if input.item(x,y,1) >= 85:
                input.itemset((x,y,1),84)

elif green_avg >= 85 and green_avg <=170:
    g_classifier = 1
    for x in range(0,final_h) :
        for y in range(0,final_w) :
            if input.item(x,y,1) <= 84:
                input.itemset((x,y,1),85)
            elif input.item(x,y,1) >= 170:
                input.itemset((x,y,1),171)

elif green_avg >= 171 and green_avg <=255:
    g_classifier = 2
    for x in range(0,final_h) :
        for y in range(0,final_w) :
            if input.item(x,y,1) <= 170:
                input.itemset((x,y,1),171)



#BLUE CHANNEL
if blue_avg >= 0 and blue_avg <=84:
    b_classifier = 0
    for x in range(0,final_h) :
        for y in range(0,final_w) :
            if input.item(x,y,2) >= 85:
                input.itemset((x,y,2),84)

elif blue_avg >= 85 and blue_avg <=170:
    b_classifier = 1
    for x in range(0,final_h) :
        for y in range(0,final_w) :
            if input.item(x,y,2) <= 84:
                input.itemset((x,y,2),85)
            elif input.item(x,y,2) >= 170:
                input.itemset((x,y,2),171)

elif blue_avg >= 171 and blue_avg <=255:
    b_classifier = 2
    for x in range(0,final_h) :
        for y in range(0,final_w) :
            if input.item(x,y,2) <= 170:
                input.itemset((x,y,2),171)





'''
#RED CHANNEL
if red_avg >= 0 and red_avg <=99:
    r_classifier = 0
    for x in range(0,final_h) :
        for y in range(0,final_w) :
            if input.item(x,y,0) >= 100:
                input.itemset((x,y,0),99)

elif red_avg >= 100 and red_avg <=199:
    r_classifier = 1
    for x in range(0,final_h) :
        for y in range(0,final_w) :
            if input.item(x,y,0) <= 99:
                input.itemset((x,y,0),100)
            elif input.item(x,y,0) >= 199:
                input.itemset((x,y,0),200)

elif red_avg >= 200 and red_avg <=255:
    r_classifier = 2
    for x in range(0,final_h) :
        for y in range(0,final_w) :
            if input.item(x,y,0) <= 199:
                input.itemset((x,y,0),200)



#GREEN CHANNEL
if green_avg >= 0 and green_avg <=99:
    g_classifier = 0
    for x in range(0,final_h) :
        for y in range(0,final_w) :
            if input.item(x,y,1) >= 100:
                input.itemset((x,y,1),99)

elif green_avg >= 100 and green_avg <=199:
    g_classifier = 1
    for x in range(0,final_h) :
        for y in range(0,final_w) :
            if input.item(x,y,1) <= 99:
                input.itemset((x,y,1),100)
            elif input.item(x,y,1) >= 199:
                input.itemset((x,y,1),200)

elif green_avg >= 200 and green_avg <=255:
    g_classifier = 2
    for x in range(0,final_h) :
        for y in range(0,final_w) :
            if input.item(x,y,1) <= 199:
                input.itemset((x,y,1),200)



#BLUE CHANNEL
if blue_avg >= 0 and blue_avg <=99:
    b_classifier = 0
    for x in range(0,final_h) :
        for y in range(0,final_w) :
            if input.item(x,y,2) >= 100:
                input.itemset((x,y,2),99)

elif blue_avg >= 100 and blue_avg <=199:
    b_classifier = 1
    for x in range(0,final_h) :
        for y in range(0,final_w) :
            if input.item(x,y,2) <= 99:
                input.itemset((x,y,2),100)
            elif input.item(x,y,2) >= 199:
                input.itemset((x,y,2),200)

elif blue_avg >= 200 and blue_avg <=255:
    b_classifier = 2
    for x in range(0,final_h) :
        for y in range(0,final_w) :
            if input.item(x,y,2) <= 199:
                input.itemset((x,y,2),200)
'''

cv.imwrite(sys.argv[3], input)
cv.imshow(sys.argv[3], input)
cv.waitKey(0)