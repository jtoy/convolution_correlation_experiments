from PIL import Image
import sys
import numpy as np
from itertools import product
import math
import cv2

file = sys.argv[1]
img = Image.open(file)
pix = np.array(img)

blur_kernel = np.zeros([5, 5]) / 5**2
blur_kernel = np.array([[1.0,2.0,1.0], [2.0,4.0,2.0], [1.0,2.0,1.0]]) / 3**2
blur_kernel = np.ones((7, 7), dtype="float") * (1.0 / (7 * 7))
blur_kernel = np.ones((5, 5), dtype="float") / 5**2
#blur_kernel = np.array(( [0, -1, 0], [-1, 5, -1], [0, -1, 0]), dtype="int") #this sharpen effect seems to make ugly images

print("shape:", pix.shape)
blurred_pix = np.zeros(pix.shape)
kernel_size = 9
def convolve(pix, kernel):
    (ph,pw) = pix.shape
    (kh,kw) = kernel.shape
    pad = math.floor(kh/2)
    output = np.zeros((ph,pw), dtype="float32")
    roi = np.zeros((kh,kw), dtype="float32")
    pix = cv2.copyMakeBorder(pix, pad, pad, pad, pad, cv2.BORDER_REPLICATE)
    for x in range(pad,pw+pad):
        for y in range(pad,ph+pad):
            roi = pix[x-pad:x+pad+1,y-pad:y+pad+1]
            #print("roi", roi.shape, " kernel ", kernel.shape)
            summed = (roi * kernel).sum()
            output[x-pad,y-pad] = summed
    return output

rpix = convolve(pix[:,:,0],blur_kernel)
gpix = convolve(pix[:,:,1],blur_kernel)
bpix = convolve(pix[:,:,2],blur_kernel)
blurred_pix = np.dstack((rpix,gpix,bpix))
print(blurred_pix.shape)
im = Image.fromarray((blurred_pix ).astype(np.uint8)) 
im.save("blurred_kernel.jpeg")

