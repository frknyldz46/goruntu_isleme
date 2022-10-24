import cv2
import numpy as np
from numpy import zeros, shape

foto = cv2.imread("baboon.jpg",0)
cv2.imshow("resim",foto)


from matplotlib import pyplot as plt
import matplotlib.image as mpimg
Hist = zeros(256)
[satir,sutun]=shape(foto)
for v in range(sutun):
    for u in range(satir):
        i=foto[u,v]
        Hist[i]=Hist[i]+1

for index in range(256):
    print(Hist[index])

cv2.waitKey()
#FURKAN YILDIZ 02200201046 NORMAL ÖĞRETİM