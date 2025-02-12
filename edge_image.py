import numpy as np
import cv2
from matplotlib import pyplot as plt
def cannyFilter(file): 
    img = cv2.imread(file, cv2.IMREAD_COLOR)
    assert img is not None, "file could not be read, check with os.path.exists()"
    edges = cv2.Canny(img,100,200)
    
    plt.subplot(121),plt.imshow(img,cmap = 'gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(edges,cmap = 'gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
    
    plt.show()

def sobelFilter(file):
    img = cv2.imread(file)
    img_blur = cv2.GaussianBlur(img, (5,5), 0)
    sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5)
    sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5)
    sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5)

    # Tried with x and y, but xy gives best image
    cv2.imshow('Sobel X', sobelx)
    cv2.waitKey(0)
    cv2.imshow('Sobel Y', sobely)
    cv2.waitKey(0)
    cv2.imshow('Sobel XY', sobelxy)
    cv2.waitKey(0)



file = 'challenge4/img.ppm'
cannyFilter(file)
sobelFilter(file)
