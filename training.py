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
for j in range(1,106,1):#change the new picture in the folder images
    print j
    image = cv2.imread('samples/'+str(j)+'.png',0)
    image=cv2.resize(image,(50,50))
#DETECTION THRESHOLD----------------------------------------------------------------------------------------------------
    T= mahotas.thresholding.otsu(image)
    for k in range(1,50,1):
        for z in range(1,50,1):
            color=image[k,z]
            if (color>T):
                image[k,z]=0
            else:
                image[k,z]=255
    thresh2=image.copy()
    keys = [i for i in range(48, 58)]
    roi_small = cv2.resize(thresh2, (10, 10))
    cv2.destroyWindow('norm')
    cv2.imshow('Numero', image)
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

