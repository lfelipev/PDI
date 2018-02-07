# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 20:16:54 2018

@author: felipe

OBS: Comentar e descomentar as funções na main() para testá-las individualmente

"""

import cv2
from matplotlib import pyplot as plt

## Calcula e plota o histograma de uma imagem em escala de cinza
def grayHist():
    # Carrega a imagem
    img = cv2.imread('lena.png', 0)
    
    # Calcula o histograma    
    hist = cv2.calcHist([img],[0],None,[256],[0,256])
    
    # Plota o histograma e a imagem ao lado
    plt.subplot(121), plt.imshow(img, 'gray')
    plt.subplot(122), plt.plot(hist)
    plt.xlim([0,256])
    plt.show()

## Calcula e plota o histograma de uma imagem colorida
# Argumento: imagem RGB
def colorHist(img):
    color = ('b', 'g', 'r')
    for i, j in enumerate(color):
        hist = cv2.calcHist([img], [i], None, [256], [0, 256])
        plt.subplot(121), plt.imshow(img, 'brg')
        plt.subplot(122), plt.plot(hist, color = j)
        plt.xlim([0, 256])
    plt.show()
    
## Adiciona um ruído de distribuição normal a uma imagem RGB
# Argumento: imagem RGB
def gaussianNoise(rgb_img):
    mean = (0,0,0)
    sigma = (150,150,150)    
    noise = rgb_img.copy()
    cv2.randn(noise, mean, sigma)
    noisy = noise + rgb_img
    colorHist(noisy)    
    
## Adiciona um ruído de distribuição uniforme a uma imagem RGB
# Argumento: imagem RGB
def uniformNoise(rgb_img):
    mean = (0,0,0)
    sigma = (50, 50, 50)
    noise = rgb_img.copy()
    cv2.randu(noise, mean, sigma)
    noisy = noise + rgb_img
    colorHist(noisy)
    
## Comentar e descomentar as funções na main() para testá-las individualmente
def main():
    ## Cria a imagem RGB
    img = cv2.imread('lena.png')
    b,g,r = cv2.split(img)
    rgb_img = cv2.merge([r, g, b])
        
    #grayHist()
    #colorHist(rgb_img)
    #gaussianNoise(rgb_img)
    uniformNoise(rgb_img)
        
if __name__ == '__main__':
    main()