#Made by Matthew Jaworski
#I pledge my honor that I have abided by the Stevens Honor System.


import random

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



quad_h = round(final_h/16)
quad_w = round(final_w/16)


########################################################################################


def quad_maker_1(start_index, end_index):
    start_modifier_x = start_index * quad_h
    end_modifier_x = start_index * quad_h
    start_modifier_y = end_index * quad_w
    end_modifier_y = end_index* quad_w

    for x in range(0 + start_modifier_x, quad_h + end_modifier_x):
        for y in range(0 + start_modifier_y,quad_w + end_modifier_y):

            input.itemset((x,y,0),modif.item(x,y,1))
            input.itemset((x,y,1),modif.item(x,y,2))
            input.itemset((x,y,2),modif.item(x,y,0))


    for x in range(0 - start_modifier_x, quad_h - end_modifier_x):
        for y in range(0 - start_modifier_y,quad_w - end_modifier_y):
            
            input.itemset((x,y,0),modif.item(x,y,1))
            input.itemset((x,y,1),modif.item(x,y,2))
            input.itemset((x,y,2),modif.item(x,y,0))

def pattern_maker_1():
    unit_amount = random.randint(5,25)

    for z in range(0, unit_amount):
        rand_x_index = random.randint(3,14)
        rand_y_index = random.randint(3,14)
        quad_maker_1(rand_x_index, rand_y_index)
        quad_maker_1(rand_y_index, rand_x_index)

        quad_maker_1(rand_x_index, rand_y_index*(-1))
        quad_maker_1(rand_y_index, rand_x_index*(-1))

        quad_maker_1(rand_x_index*(-1), rand_y_index)
        quad_maker_1(rand_y_index*(-1), rand_x_index)


########################################################################################


def quad_maker_2(start_index, end_index):
    start_modifier_x = start_index * quad_h
    end_modifier_x = start_index * quad_h
    start_modifier_y = end_index * quad_w
    end_modifier_y = end_index* quad_w

    for x in range(0 + start_modifier_x, quad_h + end_modifier_x):
        for y in range(0 + start_modifier_y,quad_w + end_modifier_y):

            input.itemset((x,y,0),modif.item(x,y,2))
            input.itemset((x,y,1),modif.item(x,y,0))
            input.itemset((x,y,2),modif.item(x,y,1))


    for x in range(0 - start_modifier_x, quad_h - end_modifier_x):
        for y in range(0 - start_modifier_y,quad_w - end_modifier_y):

            input.itemset((x,y,0),modif.item(x,y,2))
            input.itemset((x,y,1),modif.item(x,y,0))
            input.itemset((x,y,2),modif.item(x,y,1))

def pattern_maker_2():
    unit_amount = random.randint(5,25)

    for z in range(0, unit_amount):
        rand_x_index = random.randint(3,14)
        rand_y_index = random.randint(3,14)
        quad_maker_2(rand_x_index, rand_y_index)
        quad_maker_2(rand_y_index, rand_x_index)

        quad_maker_2(rand_x_index, rand_y_index*(-1))
        quad_maker_2(rand_y_index, rand_x_index*(-1))

        quad_maker_2(rand_x_index*(-1), rand_y_index)
        quad_maker_2(rand_y_index*(-1), rand_x_index)


########################################################################################


def quad_maker_3(start_index, end_index):
    start_modifier_x = start_index * quad_h
    end_modifier_x = start_index * quad_h
    start_modifier_y = end_index * quad_w
    end_modifier_y = end_index* quad_w

    for x in range(0 + start_modifier_x, quad_h + end_modifier_x):
        for y in range(0 + start_modifier_y,quad_w + end_modifier_y):

            input.itemset((x,y,0),input.item(x,y,0)+25)
            input.itemset((x,y,1),input.item(x,y,1)-25)
            input.itemset((x,y,2),input.item(x,y,2)+25)


    for x in range(0 - start_modifier_x, quad_h - end_modifier_x):
        for y in range(0 - start_modifier_y,quad_w - end_modifier_y):

            input.itemset((x,y,0),input.item(x,y,0)+25)
            input.itemset((x,y,1),input.item(x,y,1)-25)
            input.itemset((x,y,2),input.item(x,y,2)+25)

def pattern_maker_3():
    unit_amount = random.randint(5,25)

    for z in range(0, unit_amount):
        rand_x_index = random.randint(3,14)
        rand_y_index = random.randint(3,14)
        quad_maker_3(rand_x_index, rand_y_index)
        quad_maker_3(rand_y_index, rand_x_index)

        quad_maker_3(rand_x_index, rand_y_index*(-1))
        quad_maker_3(rand_y_index, rand_x_index*(-1))

        quad_maker_3(rand_x_index*(-1), rand_y_index)
        quad_maker_3(rand_y_index*(-1), rand_x_index)

########################################################################################


def quad_maker_4(start_index, end_index):
    start_modifier_x = start_index * quad_h
    end_modifier_x = start_index * quad_h
    start_modifier_y = end_index * quad_w
    end_modifier_y = end_index* quad_w

    for x in range(0 + start_modifier_x, quad_h + end_modifier_x):
        for y in range(0 + start_modifier_y,quad_w + end_modifier_y):

            input.itemset((x,y,0),input.item(x,y,2)-25)
            input.itemset((x,y,1),input.item(x,y,1)+25)
            input.itemset((x,y,2),input.item(x,y,0)-25)


    for x in range(0 - start_modifier_x, quad_h - end_modifier_x):
        for y in range(0 - start_modifier_y,quad_w - end_modifier_y):

            input.itemset((x,y,0),input.item(x,y,2)-25)
            input.itemset((x,y,1),input.item(x,y,1)+25)
            input.itemset((x,y,2),input.item(x,y,0)-25)

def pattern_maker_4():
    unit_amount = random.randint(5,25)

    for z in range(0, unit_amount):
        rand_x_index = random.randint(3,14)
        rand_y_index = random.randint(3,14)
        quad_maker_4(rand_x_index, rand_y_index)
        quad_maker_4(rand_y_index, rand_x_index)

        quad_maker_4(rand_x_index, rand_y_index*(-1))
        quad_maker_4(rand_y_index, rand_x_index*(-1))

        quad_maker_4(rand_x_index*(-1), rand_y_index)
        quad_maker_4(rand_y_index*(-1), rand_x_index)


########################################################################################


def quad_maker_5(start_index, end_index):
    start_modifier_x = start_index * quad_h
    end_modifier_x = start_index * quad_h
    start_modifier_y = end_index * quad_w
    end_modifier_y = end_index* quad_w

    for x in range(0 + start_modifier_x, quad_h + end_modifier_x):
        for y in range(0 + start_modifier_y,quad_w + end_modifier_y):

            input.itemset((x,y,0),input.item(x,y,0)+25)
            input.itemset((x,y,1),25)
            input.itemset((x,y,2),input.item(x,y,2))


    for x in range(0 - start_modifier_x, quad_h - end_modifier_x):
        for y in range(0 - start_modifier_y,quad_w - end_modifier_y):

            input.itemset((x,y,0),input.item(x,y,0)+25)
            input.itemset((x,y,1),25)
            input.itemset((x,y,2),input.item(x,y,2))

def pattern_maker_5():
    unit_amount = random.randint(5,25)

    for z in range(0, unit_amount):
        rand_x_index = random.randint(3,14)
        rand_y_index = random.randint(3,14)
        quad_maker_5(rand_x_index, rand_y_index)
        quad_maker_5(rand_y_index, rand_x_index)

        quad_maker_5(rand_x_index, rand_y_index*(-1))
        quad_maker_5(rand_y_index, rand_x_index*(-1))

        quad_maker_5(rand_x_index*(-1), rand_y_index)
        quad_maker_5(rand_y_index*(-1), rand_x_index)


########################################################################################


def quad_maker_6(start_index, end_index):
    start_modifier_x = start_index * quad_h
    end_modifier_x = start_index * quad_h
    start_modifier_y = end_index * quad_w
    end_modifier_y = end_index* quad_w

    for x in range(0 + start_modifier_x, quad_h + end_modifier_x):
        for y in range(0 + start_modifier_y,quad_w + end_modifier_y):

            input.itemset((x,y,0),modif.item(x,y,0))
            input.itemset((x,y,1),modif.item(x,y,1))
            input.itemset((x,y,2),modif.item(x,y,2))


    for x in range(0 - start_modifier_x, quad_h - end_modifier_x):
        for y in range(0 - start_modifier_y,quad_w - end_modifier_y):

            input.itemset((x,y,0),modif.item(x,y,0))
            input.itemset((x,y,1),modif.item(x,y,1))
            input.itemset((x,y,2),modif.item(x,y,2))

def pattern_maker_6():
    unit_amount = random.randint(5,25)

    for z in range(0, unit_amount):
        rand_x_index = random.randint(3,14)
        rand_y_index = random.randint(3,14)
        quad_maker_6(rand_x_index, rand_y_index)
        quad_maker_6(rand_y_index, rand_x_index)

        quad_maker_6(rand_x_index, rand_y_index*(-1))
        quad_maker_6(rand_y_index, rand_x_index*(-1))

        quad_maker_6(rand_x_index*(-1), rand_y_index)
        quad_maker_6(rand_y_index*(-1), rand_x_index)


########################################################################################


def quad_maker_7(start_index, end_index):
    start_modifier_x = start_index * quad_h
    end_modifier_x = start_index * quad_h
    start_modifier_y = end_index * quad_w
    end_modifier_y = end_index* quad_w

    for x in range(0 + start_modifier_x, quad_h + end_modifier_x):
        for y in range(0 + start_modifier_y,quad_w + end_modifier_y):

            input.itemset((x,y,0),modif.item(x,y,2))
            input.itemset((x,y,1),modif.item(x,y,2))
            input.itemset((x,y,2),modif.item(x,y,2))


    for x in range(0 - start_modifier_x, quad_h - end_modifier_x):
        for y in range(0 - start_modifier_y,quad_w - end_modifier_y):

            input.itemset((x,y,0),modif.item(x,y,2))
            input.itemset((x,y,1),modif.item(x,y,2))
            input.itemset((x,y,2),modif.item(x,y,2))

def pattern_maker_7():
    unit_amount = random.randint(5,25)

    for z in range(0, unit_amount):
        rand_x_index = random.randint(3,14)
        rand_y_index = random.randint(3,14)
        quad_maker_7(rand_x_index, rand_y_index)
        quad_maker_7(rand_y_index, rand_x_index)

        quad_maker_7(rand_x_index, rand_y_index*(-1))
        quad_maker_6(rand_y_index, rand_x_index*(-1))

        quad_maker_7(rand_x_index*(-1), rand_y_index)
        quad_maker_7(rand_y_index*(-1), rand_x_index)


########################################################################################

run_choice = random.randint(1,7)

if run_choice == 1:
    pattern_maker_1()
elif run_choice == 2:
    pattern_maker_2()
elif run_choice == 3:
    pattern_maker_3()
elif run_choice == 4:
    pattern_maker_4()
elif run_choice == 5:
    pattern_maker_5()
elif run_choice == 6:
    pattern_maker_6()
elif run_choice == 7:
    pattern_maker_7()


#cv.imwrite(sys.argv[3], input)
cv.imshow(sys.argv[3], input)
cv.waitKey(0)