import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread(input)
cv.imshow('Original', img)

#histogram creation

plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors = ('b','g','r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img],[i], None, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])

plt.show()

cv.waitKey(0)