from sklearn.neighbors  import KNeighborsClassifier

import cv2;
import pickle;
import numpy as np;
import os;

video = cv2.VideoCapture(0);
face_detect = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml');

with open('data/names.pkl' , 'rb')  as f:
    Labels = pickle.load(f);
with open('data/faces_data.pkl' , 'rb')  as f:
    Faces = pickle.load(f);

knn = KNeighborsClassifier(n_neighbors=5);
knn.fit(Faces,Labels);


while True:
    ret,frame  = video.read();
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY);
    faces = face_detect.detectMultiScale(gray,1.3 , 5);
    for (x,y,w,h) in faces :
        crop_image = frame[y:y+h , x:x+w,:];
        resized_image = cv2.resize(crop_image,(50,50)).flatten().reshape(1,-1);
        output = knn.predict(resized_image);
        cv2.putText(frame,str(output[0]) , (x,y-15), cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255) ,1);
        
        cv2.rectangle(frame, (x,y) , (x+w, y+h), (50,50,255) ,1);
    cv2.imshow("Video capture",frame);
    w = cv2.waitKey(1);
    if w == ord('q'):
        break;
video.release();
cv2.destroyAllWindows();


