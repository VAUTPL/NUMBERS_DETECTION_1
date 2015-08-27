__author__ = 'valeria'
import cv2
import numpy as np
def region(image12,gris,gray1,image):
    contorno=cv2.Canny(image12,50,120)
    (cnts, _) = cv2.findContours(contorno.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cnts = sorted([(c, cv2.boundingRect(c)[0]) for c in cnts], key = lambda x: x[1])
    for (c,_) in cnts:
        (x, y, w, h) = cv2.boundingRect(c)
        if (w)>100:
            co=gris[y:y+h,x:x+w]
            b=gris[y+5,x+5]
            if (w>=200) & (w<700) & (h>20)&(h<120):
                co=gris[y-5:y+h+5,x-5:x+w+5]
                mascaracon=np.zeros(image.shape[:2], dtype="uint8")
                cv2.rectangle(mascaracon, (x+2,y+2), (x+w+10, y+h+5), 255, -1)
                imagencon=cv2.bitwise_and(gray1,gray1,mask=mascaracon)
                image14=imagencon.copy()
    return image14
def recon_borde(image):
    image=cv2.resize(image,(50,50))
    gray2=cv2.equalizeHist(image)
    blur = cv2.GaussianBlur(gray2,(5,5),0)
    ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    #EDGE DETECTION-----------------------------------------------------------------------------------------------------
    edged = cv2.Canny(th3, 20, 80)
    thresh = cv2.adaptiveThreshold(edged, 255, 1, 1, 11, 2)
    return thresh
def concatenar(results,contador,digito):
            digito=(results[0][0])*(10**contador)
            return digito