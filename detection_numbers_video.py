#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-#
# PROJECT   : DETECTION OF NUMBERS IN ELECTRIC METER                                               #
# VERSION   : 1.0                                                                                                      #
# AUTHOR    : Valeria Quinde Granda             valeestefa15@gmail.com                                                 #
# PROFESSOR : Rodrigo Barba                     lrbarba@utpl.edu.ec                                                    #
# COMPANY   : Sic ElectriTelecom  Loja-Ecuador                                                                         #
# DATE      : 26/08/2015                                                                                               #
#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-#
#IMPORT LIBRARIES-------------------------------------------------------------------------------------------------------
import cv2
import numpy as np
import MySQLdb
import mahotas
import time
import support_library
#ADRESS DATABASE--------------------------------------------------------------------------------------------------------
DB_HOST = '199.168.189.114'
DB_PORT = '3306'
DB_USER = 'mancomun_opencv'
DB_PASS = 'QGPhx}SzV~y6'
DB_NAME = 'mancomun_opencv'
#TRAINING---------------------------------------------------------------------------------------------------------------
samples = np.loadtxt('data/general_samples.data', np.float32)
responses = np.loadtxt('data/general_responses.data', np.float32)
responses = responses.reshape((responses.size,1))
digito=0
model = cv2.KNearest()
model.train(samples, responses)
rois=220
xf=90
xfx=xf
contador=1
#-----------------------------------------------------------------------------------------------------------------------
print "PRESIONA c PARA CORTAR LA REGION DE INTERES"
nombre=(raw_input("INGRESE EL NOMBRE DEL VIDEO O CAMARA PARA TOMAR FOTO:"))
if nombre=='camara':
    camara=cv2.VideoCapture(0)
else:
    camara=cv2.VideoCapture('images/'+nombre+'.mp4')
while True:
    (grabacion, img) = camara.read()
    imagen = cv2.resize(img, (800, 500))
    cv2.rectangle(imagen, (xf, rois), (xf+700, rois+70), (0, 25, 255), 1)
    cv2.putText(imagen, "REGION DE INTERES", (xf, rois-10), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 2)
    cv2.imshow("CAMARA",imagen)
    tecla=cv2.waitKey(1)
    if tecla==ord('c'):
        image=img
        break
#CONVERTING THE IMAGE TO GRAYSCALE--------------------------------------------------------------------------------------
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
#FILTER-----------------------------------------------------------------------------------------------------------------
blurred = cv2.GaussianBlur(image1, (5,7),0)
blurred = cv2.medianBlur(blurred,1)
#THRESHOLD--------------------------------------------------------------------------------------------------------------
v = np.mean(blurred)
sigma=0.1
lower = (int(max(0, (2.0 - sigma) * v)))
upper = (int(min(255, (2.0 + sigma) * v)))
#EDGE DETECTION---------------------------------------------------------------------------------------------------------
edged = cv2.Canny(blurred, lower, upper)
(cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cnts = sorted([(c, cv2.boundingRect(c)[0]) for c in cnts], key = lambda x: x[1])
yf=rois
vec=[]
contador=4
contador2=1
#EDGE RECOGNITION-------------------------------------------------------------------------------------------------------
consumo=0
for (c,_) in cnts:
    (x, y, w, h) = cv2.boundingRect(c)
    if w > 10 and h > 10 and w<50:
      if(x-xfx)>10:
        if contador2<6:
                xfx=x+w
                yf=y
                roi2=gris[y:y+h,x:x+w]
                roi=support_library.recon_borde(roi2)
                roi_small = cv2.resize(roi,(10,10))
                roi_small = roi_small.reshape((1,100))
                roi_small = np.float32(roi_small)
                retval, results, neigh_resp, dists = model.find_nearest(roi_small, k = 1)
                string = str(int((results[0][0])))
                cv2.putText(image, str(string), (x - 10, y - 10),cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 2)
                cv2.imshow("final",image)
                cv2.waitKey(0)
#CONCATENATE NUMBERS----------------------------------------------------------------------------------------------------
                digito=support_library.concatenar(results,contador,digito)
                consumo=int(consumo)+int(digito)
                contador2=contador2+1
                contador-=1
print 'El numero facturado es:',consumo
fecha_captura = time.strftime("%d/%m/%y")
hora_captura = time.strftime("%H:%M:%S")
print 'La fecha:',fecha_captura,'y hora:',hora_captura
cv2.waitKey(0)
#SENDING DATA OBTAINED THE DATABASE-------------------------------------------------------------------------------------
#bd = MySQLdb.connect(DB_HOST,DB_USER, DB_PASS, DB_NAME)
#cursor = bd.cursor()
#try:
#    cursor.execute("INSERT INTO detect_numbers (consumo,fecha,hora) VALUES (%s,%s, %s)", (consumo,fecha_captura, hora_captura))
#    bd.commit()
#    cursor.close()
#except:
#    bd.rollback()
#bd.close()