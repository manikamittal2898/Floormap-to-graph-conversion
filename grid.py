import cv2
import numpy as np

im =  cv2.imread("office_floor_plan.png")
im = cv2.resize(im,(1000,500))
num_of_tiles=400
imgheight=im.shape[0]  
imgwidth=im.shape[1]



y1 = 0
M = imgheight//20
N = imgwidth//20

for y in range(0,imgheight,M):
    for x in range(0, imgwidth, N):
        y1 = y + M
        x1 = x + N
        tiles = im[y:y+M,x:x+N]

        cv2.rectangle(im, (x, y), (x1, y1), (0, 255, 0))
        cv2.imwrite("save/" + str(x) + '_' + str(y)+".png",tiles)

cv2.imwrite("asas.png",im)
