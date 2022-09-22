from PIL import Image
import sys
import numpy as np
from itertools import product
import math
file = sys.argv[1]
img = Image.open(file)
pix = np.array(img)

#im just using an average instead of weighted average to make it easy to compute with a for loop, but normally you would use a weight matrix.
#I also dont know how a blur weight matrix is derived, but seems easily to make one where the center has higher weights

def kernel(x,y,rgb,pix, kernel_size=3):
    #kernel_size must be odd number
    diff = math.floor(kernel_size/2)
    if x - diff  < 0:
        xx = 0
    else:
        xx = x - diff
    if y - diff < 0:
        yy = 0
    else:
        yy = y - diff
    if x + diff+1 < pix.shape[0]:
        xxx = x + diff+1
    else:
        xxx = pix.shape[0]
    if y + diff+1 < pix.shape[0]:
        yyy = y + diff+1
    else:
        yyy = pix.shape[0]
    pixel_sum = 0
    total = 0
    #print("x start",xx, "x end ", xxx, " y start", yy, " y end ",yyy)
    for xn in range(xx,xxx):
        for yn in range(yy,yyy):
            #print("x start",xx, "x end ", xxx, " y start", yy, " y end ",yyy, " xn ", xn, " yn ",yn)
            total += 1
            pixel_sum += pix[xn][yn][rgb]
    #print(total)
    return(pixel_sum/total)
            




print("shape:", pix.shape)
blurred_pix = np.zeros(pix.shape)
kernel_size = 9
for x in range(pix.shape[0]):
    for y in range(pix.shape[1]):
        r = kernel(x,y,0,pix,kernel_size)
        g = kernel(x,y,1,pix,kernel_size)
        b = kernel(x,y,2,pix,kernel_size)
        blurred_pix[x][y][0] = r
        blurred_pix[x][y][1] = g
        blurred_pix[x][y][2] = b
        
        #print(pix[x][y])
#im = Image.fromarray(blurred_pix)
#need this bc of here: https://stackoverflow.com/questions/55319949/pil-typeerror-cannot-handle-this-data-type
print("new shape:", blurred_pix.shape)
im = Image.fromarray((blurred_pix ).astype(np.uint8)) 
im.save("burred.jpeg")

