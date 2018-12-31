# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 16:35:30 2018

@author: dilu
"""

# Reference: http://10.1.2.209/face_recognition/DiluFaceTrain/blob/master/examples/kaggle_fkd/predict_landmark.py


import cv2
import matplotlib.pyplot as plt

img_path = '.img/Aaron_Eckhart_0001.jpg'
img = cv2.imread(img_path)
#print(img.shape)

landmarks = []
txt_path = './Aaron_Guiel_0002_5loc_attri.txt'
with open(txt_path) as f:
    for pos in f.readlines():
        landmarks.append(pos.strip())

for i in landmarks:
    j = i.split(" ")
    x = int(float(j[0]))
    #print(x)
    y = int(float(j[1]))
    print(x, y)
    pos = (x, y)
    img = cv2.circle(img, pos, 1, (0, 255, 0), -1)
    
plt.imshow(img)
plt.savefig("landmark.jpg")
plt.show()
