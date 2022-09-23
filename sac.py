from PIL import Image
import sys
import numpy as np
from itertools import product
import cv2
import scipy
#sin and checkered patterns and symetrical stuff , 256
file = sys.argv[1]
img = Image.open(file)
pix = np.array(img)

kernel = np.ones((5, 5), dtype="float") / 5**2
print("shape", pix.shape)

kernel_size = 9
def convolve(pix, kernel):
    (ph,pw) = pix.shape
    (kh,kw) = kernel.shape
    pad = kh//2
    output = np.zeros((ph,pw), dtype="float32")
    roi = np.zeros((kh,kw), dtype="float32")
    pix = cv2.copyMakeBorder(pix, pad, pad, pad, pad, cv2.BORDER_REPLICATE)
    for x in range(pad,pw+pad):
        for y in range(pad,ph+pad):
            roi = pix[x-pad:x+pad+1,y-pad:y+pad+1]
            roi = pix[x-pad:x+pad,y-pad:y+pad]
            #print("roi", roi.shape, " kernel ", kernel.shape)
            summed = (roi * kernel).sum()
            output[x-pad,y-pad] = summed
    return output

# from https://www.anycodings.com/1questions/5817325/shifting-an-image-in-numpy
def shift_image(X, dx, dy):
    X = np.roll(X, dy, axis=0)
    X = np.roll(X, dx, axis=1)
    if dy>0:
        X[:dy, :] = 0
    elif dy<0:
        X[dy:, :] = 0
    if dx>0:
        X[:, :dx] = 0
    elif dx<0:
        X[:, dx:] = 0
    return X

shifted_pix = shift_image(pix,20,30)
sacr = convolve(pix[:,:,0],pix[:,:,0])
sacg = convolve(pix[:,:,1],pix[:,:,1])
sacb = convolve(pix[:,:,2],pix[:,:,2])
sac_pix = np.dstack((sacr,sacg,sacb))
im = Image.fromarray((sac_pix ).astype(np.uint8)) 

im.save("sac.jpg")

