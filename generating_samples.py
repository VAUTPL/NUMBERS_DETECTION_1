#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-#
# PROJECT   : DETECTION OF NUMBERS IN ELECTRIC METER(GENERATING SAMPLES)                                               #
# VERSION   : 1.0                                                                                                      #
# AUTHOR    : Valeria Quinde Granda             valeestefa15@gmail.com                                                 #
# PROFESSOR : Rodrigo Barba                     lrbarba@utpl.edu.ec                                                    #
# COMPANY   : Sic ElectriTelecom  Loja-Ecuador                                                                         #
# DATE      : 26/08/2015                                                                                               #
#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-#
#IMPORT LIBRARIES-------------------------------------------------------------------------------------------------------
import cv2
import numpy as np
import mahotas
xi=90
contador=1
rois=100
cont=1
#LOAING IMAGE-----------------------------------------------------------------------------------------------------------
for cont in range(1,23,1):#change the new picture in the folder images
    xf=1
    xfx=xf
    image = cv2.imread('images/'+'img'+str(cont)+'.jpg')
    image = cv2.resize(image, (800, 500))
    cv2.imshow("imagen original",image)
    gris = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    mascar=np.zeros(image.shape[:2], dtype="uint8")
    cv2.rectangle(mascar, (xf, rois), (xf+800, rois+90), 255, -1)
    image2=cv2.bitwise_and(gris,gris,mask=mascar)
    T3=mahotas.thresholding.otsu(image2)
    gris_copy=gris.copy()
    gris_2=gris.copy()
#NEGATIVE IMAGE---------------------------------------------------------------------------------------------------------
    for j in range(1,800,1):
        for i in range(1,500,1):
            color=gris[i,j]
            gris[i,j]=255-color
    gris=cv2.GaussianBlur(gris, (3, 3),0)
    T1=mahotas.thresholding.otsu(gris)
    clahe = cv2. createCLAHE(clipLimit=1.0)
    grises= clahe . apply(gris)
    conteo=1
    T2 = mahotas.thresholding.otsu(grises)
    T=(T2+T1+5)/2
#THRESHOLD--------------------------------------------------------------------------------------------------------------
    for k in range(rois,rois+90,1):
        for z in range(xf,800,1):
            color=grises[k,z]
            if color>T:
                grises[k,z]=0
            else:
                grises[k,z]=255
#MASCARA FOR ROI--------------------------------------------------------------------------------------------------------
    mascara=np.zeros(image.shape[:2], dtype="uint8")
    cv2.rectangle(mascara, (xf, rois), (xf+800, rois+90), 255, -1)
    image1=cv2.bitwise_and(grises,grises,mask=mascara)
#FILTER-----------------------------------------------------------------------------------------------------------------
    blurred = cv2.GaussianBlur(image1, (7,7),0)
    blurred = cv2.medianBlur(blurred,1)
#THRESHOLD FOR DETECTION OF EDGES--------------------------------------------------------------------------------------------------------------
    v = np.mean(blurred)
    sigma=0.33
    lower = (int(max(0, (1.0 - sigma) * v)))
    upper = (int(min(255, (1.0 + sigma) * v)))
#EDGE DETECTION---------------------------------------------------------------------------------------------------------
    edged = cv2.Canny(blurred, lower, upper)
    (cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    cnts = sorted([(c, cv2.boundingRect(c)[0]) for c in cnts], key = lambda x: x[1])
    yf=rois
    vec=[]
    contador2=1
#EDGE RECOGNITION-------------------------------------------------------------------------------------------------------
    consumo=0
    for (c,_) in cnts:
        (x, y, w, h) = cv2.boundingRect(c)
        if w > 11 and h > 14 and w<100:
          if(x-xfx)>10:
            if contador2<6:
                    xfx=x+w
                    yf=y
                    roi=gris[y:y+h,x:x+w]
                    guardar=roi.copy()
                    cv2.imshow("roi",roi)
                    cv2.imwrite(("samples/"+str(contador)+'.png'),guardar)
                    contador2+=1
                    contador+=1

