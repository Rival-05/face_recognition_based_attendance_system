from sklearn.neighbors  import KNeighborsClassifier;
import cv2;
import pickle;
import numpy as np;
import os;
import csv;
import time;
from datetime import datetime;

with open('data/names.pkl' , 'rb')  as f:
    Labels = pickle.load(f);
with open('data/faces_data.pkl' , 'rb')  as f:
    Faces = pickle.load(f);

knn = KNeighborsClassifier(n_neighbors=5);
knn.fit(Faces,Labels);

video = cv2.VideoCapture(0);
face_detect = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml');
COL_Name = ["Name" , "Time"];
while True:
    ret,frame  = video.read();
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY);
    faces = face_detect.detectMultiScale(gray,1.3 , 5);
    for (x,y,w,h) in faces :
        crop_image = frame[y:y+h , x:x+w,:];
        resized_image = cv2.resize(crop_image,(50,50)).flatten().reshape(1,-1);

        distances, indices = knn.kneighbors(resized_image);
        if distances[0][0] > 5300:  
            output = "Unknown"
        else:
            output = knn.predict(resized_image)[0];
        
        ts = time.time();
        date = datetime.fromtimestamp(ts).strftime("  %d-%m-%y");
        Current_time = datetime.fromtimestamp(ts).strftime("%H:%M:%S");
        attendance = [str(output) , str(Current_time)];
        file_exist = os.path.isfile("Attendance/Attendance_" + date + ".csv")

        color = (0, 255, 0) if output != "Unknown" else (0, 0, 255)
        cv2.putText(frame,str(output) , (x,y-15), cv2.FONT_HERSHEY_COMPLEX,1,color ,1);        
        cv2.rectangle(frame, (x,y) , (x+w, y+h), color ,1);
    cv2.imshow("Video capture",frame);
    w = cv2.waitKey(1);
    if w == ord('m'):
        time.sleep(1);
        if file_exist :
            with open("Attendance/Attendance_" + date + ".csv","+a") as csvfile:
                writer = csv.writer(csvfile);
                writer.writerow(attendance);
            csvfile.close();
        else:
            with open("Attendance/Attendance_" + date +".csv","+a") as csvfile:
                writer = csv.writer(csvfile);
                writer.writerow(COL_Name);
                writer.writerow(attendance);
            csvfile.close();
    if w == ord('q'):
        break;
video.release();
cv2.destroyAllWindows();


