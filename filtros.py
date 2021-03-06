# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 20:16:54 2018

@author: felipe

OBS: Comentar e descomentar as funções na main() para testá-las individualmente

"""

import cv2
from matplotlib import pyplot as plt

def medianBlurring():
    img = cv2.imread('105053.png')
    median = cv2.medianBlur(img, 5)
    plt.subplot(121), plt.imshow(img), plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(median), plt.title('Filtered')
    plt.xticks([]), plt.yticks([])    
    plt.show()

def gaussianBlurring():
    img = cv2.imread('105053.png')
    median = cv2.GaussianBlur(img, (5,5), 0)
    plt.subplot(121), plt.imshow(img), plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(median), plt.title('Filtered')
    plt.xticks([]), plt.yticks([])    
    plt.show()

def bilateralFilter():
    img = cv2.imread('105053.png')
    median = cv2.bilateralFilter(img, 9, 75, 75)
    plt.subplot(121), plt.imshow(img), plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(median), plt.title('Filtered')
    plt.xticks([]), plt.yticks([])    
    plt.show()
    
## Comentar e descomentar as funções na main() para testá-las individualmente
def main():
    #bilateralFilter()
    #aussianBlurring()
    medianBlurring()
        
if __name__ == '__main__':
    main()