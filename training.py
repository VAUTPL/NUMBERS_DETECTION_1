#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-#
# PROJECT   : DETECTION OF NUMBERS IN ELECTRIC METER(TRAINING)                                                         #
# VERSION   : 1.0                                                                                                      #
# AUTHOR    : Valeria Quinde Granda             valeestefa15@gmail.com                                                 #
# PROFESSOR : Rodrigo Barba                     lrbarba@utpl.edu.ec                                                    #
# COMPANY   : Sic ElectriTelecom  Loja-Ecuador                                                                         #
# DATE      : 26/08/2015                                                                                               #
#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-#
import numpy as np
import cv2
import mahotas
# OPEN TRAINING IMAGE FOR PROCESSING------------------------------------------------------------------------------------
samples =  np.empty((0, 100))
responses = []
for j in range(1,81,1):
    print j
    image = cv2.imread('samples/'+str(j)+'.png')
    image=cv2.resize(image,(50,50))
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray2=cv2.equalizeHist(gray)
    blur = cv2.GaussianBlur(gray2,(5,5),0)
    ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    cv2.waitKey(0)
    #EDGE DETECTION-----------------------------------------------------------------------------------------------------
    edged = cv2.Canny(th3, 20, 80)
    cv2.imshow("canny",edged)
    thresh = cv2.adaptiveThreshold(edged, 255, 1, 1, 11, 2)
    thresh2=thresh.copy()
    cv2.imshow("thresh",thresh)
    cv2.waitKey(0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    keys = [i for i in range(48, 58)]
    for contour in contours:
            [x, y, w, h] = cv2.boundingRect(contour)
            if h > 10:
                cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)
                roi = thresh2[y:y+h, x:x+w]
                cv2.imshow("imagen",roi)
                roi_small = cv2.resize(roi, (10, 10))
                cv2.imshow('norm', image)
                key = cv2.waitKey(0)
                if key == 27:
                   cv2.destroyAllWindows()
                elif key in keys:
                    sample = roi_small.reshape((1,100))
                    samples = np.append(samples,sample,0)
                    responses.append(int(chr(key)))
print "training complete"
np.savetxt('data/general_samples.data', samples)
responses = np.array(responses, np.float32)
responses = responses.reshape((responses.size,1))
np.savetxt('data/general_responses.data', responses)

