__author__ = 'valeria'
import cv2
import numpy as np
import mahotas
#THRESHOLD FOR DETECTION------------------------------------------------------------------------------------------------
def recon_borde(image):
    image=cv2.resize(image,(50,50))
    t= mahotas.thresholding.otsu(image)
    for k in range(1,50,1):
        for z in range(1,50,1):
            color=image[k,z]
            if color>t:
                image[k,z]=0
            else:
                image[k,z]=255
    thresh = image.copy()
    return thresh
#CONCATENATE OF NUMBERS-------------------------------------------------------------------------------------------------
def concatenar(results,contador,digito):
            digito=(results[0][0])*(10**contador)
            return digito