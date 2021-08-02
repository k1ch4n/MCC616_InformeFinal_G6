# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 22:59:17 2021

@author: Roberto
"""
import cv2
#import os

root='D:\\video_mano\\out2_train.mp4'
cam=cv2.VideoCapture(root)
suma=cam.get(7)
time=(int)(suma/500)
suma=0

currentframe=0

while True:
    ret,frame=cam.read()
    suma += 1
    if ret == False:
        break
    if suma % time == 0 and currentframe<500:
        name= str(currentframe+1)+'.jpg'
        print('creando... '+name)
        cv2.imwrite(name,frame)
        currentframe +=1
cam.release()
cv2.destroyAllWindows()