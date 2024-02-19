import numpy as np
from skimage import data,io
import matplotlib.pyplot as plt

def get(im, i, j):
    if 0 <= i < im.shape[0] and 0 <= j < im.shape[1]:
        return im[i, j]
    return 0

def GAP(im, i, j):
    In = get(im, i, j-1)
    Iw = get(im, i-1, j)
    Ine = get(im, i+1, j-1)
    Inw = get(im, i-1, j-1)
    Inn = get(im, i, j-2)
    Iww = get(im, i-2, j)
    Inne = get(im, i+1, j-2)
    dh = abs(Iw - Iww) + abs(In - Inw) + abs(In - Ine)
    dv = abs(Iw - Inw) + abs(In - Inn) + abs(Ine - Inne)
    if dv - dh > 80: #sharp horizontal edge
        return Iw
    elif dv - dh < -80: #sharp vertical edge
        return In
    else:
        ic = (Iw + In) / 2 + (Ine - Inw) / 4
        if dv - dh > 32: # horizontal edge
            return (ic + Iw) / 2 
        elif dv - dh > 8: #weak horizontal edge
            return (3*ic + Iw) / 4
        elif dv - dh < -32: # vertical edge
            return (ic + In) / 2
        elif dv - dh < -8: # weak vertical edge
            return (3*ic + In) / 4
        return ic


im = data.camera() # is gray scale image.
out = np.empty((im.shape[0], im.shape[1])) # Icap

for i in range(im.shape[0]):
    for j in range(im.shape[1]):
        out[i, j] = GAP(im, i, j)
