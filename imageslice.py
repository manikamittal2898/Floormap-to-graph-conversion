import image_slicer
from PIL import ImageDraw, ImageFont
import PIL.Image
import cv2
import numpy as np
num_of_tiles=400
tiles=image_slicer.slice(r'dotted_bounds.png', num_of_tiles)

arr=np.zeros([num_of_tiles, 1])
i=0

for tile in tiles:
   # print(tile.image.format, tile.image.size, tile.image.mode)
   # print(tile.image.getextrema())
   # tile.image.show()
   pil_image = tile.image.convert('RGB') 
   open_cv_image = np.array(pil_image) 
# Convert RGB to BGR 
   img = open_cv_image[:, :, ::-1].copy()
   img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
   mask1 = cv2.inRange(img_hsv, (0,50,20), (5,255,255))
   mask2 = cv2.inRange(img_hsv, (175,50,20), (180,255,255))
   mask = cv2.bitwise_or(mask1, mask2)

# Determine if the color exists on the image
   if cv2.countNonZero(mask) > 0:
      arr[i]=1
      # print('Red is present!')
   # else:
   #    print('Red is not present!')
      # arr[i]=0
   i=i+1

graph = np.reshape(arr, (20, 20))
print(graph)
   