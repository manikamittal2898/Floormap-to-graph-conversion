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
   # mask1 = cv2.inRange(img_hsv, (0,50,20), (5,255,255))
   # mask2 = cv2.inRange(img_hsv, (175,50,20), (180,255,255))
   # mask = cv2.bitwise_or(mask1, mask2)
   # mask3 = cv2.inRange(img_hsv, (40,240,20), (45,255,255))
   redmask=cv2.inRange(img_hsv,(169,215,197),(189,235,277))
   yellowmask=cv2.inRange(img_hsv,(20,245,215),(40,265,295))
   bluemask=cv2.inRange(img_hsv,(108,166,164),(128,186,244))
   greenmask=cv2.inRange(img_hsv,(59,196,137),(79,216,217))
   pinkmask=cv2.inRange(img_hsv,(155,117,215),(175,137,295))
# Determine if red color exists on the image
   if cv2.countNonZero(redmask) > 0:
      arr[i]=1
      #yellow means destination is to the south
      if cv2.countNonZero(yellowmask) > 0:
         arr[i]=2
      #blue means destination is to the left
      if cv2.countNonZero(bluemask) > 0:
         arr[i]=4
      #pink means destination is to the north
      if cv2.countNonZero(pinkmask) > 0:
         arr[i]=3
      #green means destination is to the right
      if cv2.countNonZero(greenmask) > 0:
         arr[i]=5
   i=i+1

graph = np.reshape(arr, (20, 20))
print(graph)
   