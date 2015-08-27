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
contador=31
rois=115
cont=1
#CONVERTING THE IMAGE TO GRAYSCALE--------------------------------------------------------------------------------------
for cont in range(1,11,1):
    xf=1
    xfx=xf
    image = cv2.imread('images/'+'img'+str(cont)+'.jpg')
    image = cv2.resize(image, (800, 500))
    gris = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Imagen original", image)
    cv2.waitKey(0)
    gray = gris.copy()
    #CONTRAST LEVELING------------------------------------------------------------------------------------------------------
    clahe = cv2 . createCLAHE(clipLimit=2.0)
    gray = clahe . apply(gray)
    gray1=gray.copy()
    umbral=mahotas.thresholding.otsu(gris)
    gray1[gray1 > umbral] = 255
    gray1[gray1 < umbral] = 0
    #REGION OF INTEREST-----------------------------------------------------------------------------------------------------
    mascara=np.zeros(image.shape[:2], dtype="uint8")
    cv2.rectangle(mascara, (xf, rois), (xf+800, rois+70), 255, -1)
    image1=cv2.bitwise_and(gray1,gray1,mask=mascara)
    cv2.imshow("Recorte", image1)
    #FILTER-----------------------------------------------------------------------------------------------------------------
    blurred = cv2.GaussianBlur(image1, (5,7),0)
    blurred = cv2.medianBlur(blurred,1)
    cv2.imshow("filtro",blurred)
    #THRESHOLD--------------------------------------------------------------------------------------------------------------
    v = np.mean(blurred)
    sigma=0.1
    lower = (int(max(0, (2.0 - sigma) * v)))
    upper = (int(min(255, (2.0 + sigma) * v)))
    cv2.waitKey(0)
    #EDGE DETECTION---------------------------------------------------------------------------------------------------------
    edged = cv2.Canny(blurred, lower, upper)
    cv2.imshow("blurred2",edged)
    cv2.waitKey(0)
    (cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cnts = sorted([(c, cv2.boundingRect(c)[0]) for c in cnts], key = lambda x: x[1])
    yf=rois
    vec=[]
    contador2=1
    #EDGE RECOGNITION-------------------------------------------------------------------------------------------------------
    numero=0
    for (c,_) in cnts:
        (x, y, w, h) = cv2.boundingRect(c)
        i=1
        q=800
        if w > 10 and h > 10 and w<50:
          if(x-xfx)>10:
            if contador2<6:
                xfx=x+w
                yf=y
                roi = image[y:y + h, x:x + w]
                guardar=roi.copy()
                cv2.imshow("roi",roi)
                cv2.imwrite(("samples/"+str(contador)+'.png'),guardar)
                contador2+=1
                contador+=1
                cv2.waitKey(0)

