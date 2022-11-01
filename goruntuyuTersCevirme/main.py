import cv2
import numpy as np
from matplotlib import pyplot as plt
resim = cv2.imread('baboon.jpg',0)

cv2.imshow("orjinal",resim)

[h,w] = resim.shape

for i in range(h):
    for j in range(w):
        resim[i,j] = np.max(resim) - resim[i,j]


cv2.imshow("Terslenmis",resim)
cv2.waitKey()