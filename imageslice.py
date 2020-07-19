import image_slicer
from PIL import ImageDraw, ImageFont
import PIL.Image
import cv2
import numpy as np
from image_slicer import join
from PIL import Image
import copy
import easygui
import pandas as pd

df = pd.DataFrame(columns = ['Node', 'Row','Column'])
num_of_tiles=400
tiles=image_slicer.slice(r'dotted_bounds.png', num_of_tiles, save=False)
stiles = copy.deepcopy(tiles)
arr=np.zeros([num_of_tiles, 1])
# d=np.empty(num_of_tiles, dtype='object')
i=0
k=0

for tile in tiles:
   pil_image = tile.image.convert('RGB') 
   open_cv_image = np.array(pil_image) 
# Convert RGB to BGR 
   img = open_cv_image[:, :, ::-1].copy()
   img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
  
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
      # Code to add name of destination
      if arr[i]==2 or arr[i]==3 or arr[i] == 4 or arr[i] ==5:
         tile.image = Image.open(r"animate.png")
         image_src = join(tiles)
         image_src.show()
         dest = easygui.enterbox("Enter the name of the destination node")
         tile.image = stiles[i].image
         # d[i]=dest
         # dest=k
         df.loc[k]=[dest,19-(i//20),i%20]
         k+=1
         
   i=i+1

graph = np.reshape(arr, (20, 20))
print(graph)
print(df)  
df.to_csv("Nodes.csv", index=False)