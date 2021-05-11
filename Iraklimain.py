import cv2 as cv
import numpy as np
import sys

#input and load images
debug = "false";
if len(sys.argv) != 4 or len(sys.argv) == 5 :
    if len(sys.argv) == 5 :
        if sys.argv[4] != "debug" :
            sys.exit("Pass 3 arguments, input image name, blurring output name and sharpening output name")
        elif sys.argv[4] == "debug":
            debug = "true"
    else :
        sys.exit("Pass 3 arguments, input image name, blurring output name and sharpening output name")

input = cv.imread(sys.argv[1])
if input is None :
    sys.exit("Could not read input")
in_h, in_w, in_c = input.shape






# Blurring

box filter
kernel = (1/9)*np.array([[1,1,1],
                            [1,1,1],
                             [1,1,1]])
newImgB = np.zeros_like(input)
height, width, _ = input.shape
for k in range(1, height-1):
    for l in range(1, width-1):
        newImgB[k, l] = sum(sum(kernel * input[k-1:k+2, l-1:l+2]))

if debug == "true" :
    print("Final resolution: " + str(in_w) + " by " + str(in_h))
    cv.imshow("Raw Input", input)
    cv.imshow("Blurriness Applied", newImgB)
    cv.waitKey(0)



#Sharpening

kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
height, width, _ = input.shape
inputBW = np.zeros((height, width))
newImgS = np.zeros_like(inputBW)
newImgSColor = np.zeros_like(input)

for k in range(0, height):
    for l in range(0, width):
        inputBW[k, l] = sum(input[k, l])//3

for k in range(1, height-1):
    for l in range(1, width-1):
        newImgS[k, l] = sum(sum(kernel * inputBW[k-1:k+2, l-1:l+2]))

print(input[0][0])

for k in range(1, height-1):
    for l in range(1, width-1):
        filteredBWIntensity = newImgS[k, l]
        originalBWIntensity = sum(input[k, l])//3
        ratioOfIntensityChange = filteredBWIntensity/originalBWIntensity
        newImgSColor[k, l] = list(map(lambda x: min(255, x), ratioOfIntensityChange * input[k, l]))

if debug == "true" :
    print("Final resolution: " + str(in_w) + " by " + str(in_h))
    cv.imshow("Raw Input", input)
    cv.imshow("Sharpness Applied", newImgS)
    cv.waitKey(0)

cv.imwrite(sys.argv[2], newImgB)
cv.imwrite(sys.argv[3], newImgSColor)

