import cv2
import numpy as np
import face_recognition
import keyboard
import os
from datetime import datetime
# from PIL import ImageGrab
 
path = 'ImagesAttendance'
images = []
classNames = []
myList = os.listdir(path)
print(myList)


for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
    
 
print(len(images))

def findEncodings(images):
    print(len(images))
    encodeList = []
    for img in images:
        print("hey")
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)   
    return encodeList


def exit_program():
    cap.release()  # Release the webcam
    cv2.destroyAllWindows()  # Close all OpenCV windows
    print("Program terminated gracefully.")
    exit(0)


exit_key = "q"


    
def markAttendance(name):
    with open('Attendance.csv','r+') as f:
        print("heythere")
        myDataList = f.readlines()
        print(myDataList)
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
            print(nameList)
            
            
        if name not in nameList:
                now = datetime.now()
                dtString = now.strftime('%H:%M:%S')
                f.writelines(f'{name},{dtString}\n')
        
    #### FOR CAPTURING SCREEN RATHER THAN WEBCAM
    # def captureScreen(bbox=(300,300,690+300,530+300)):
    #     capScr = np.array(ImageGrab.grab(bbox))
    #     capScr = cv2.cvtColor(capScr, cv2.COLOR_RGB2BGR)
    #     return capScr
 
encodeListKnown = findEncodings(images)
print('Encoding Complete')
print(len(encodeListKnown))
#Initialising webcam 
cap = cv2.VideoCapture(0)
 
while True:
    #img is the frame, success is a boolean value that is true if the frame is read correctly
    
    if keyboard.is_pressed(exit_key):
        exit_program()
    success, img = cap.read()
    #img = captureScreen()
    imgS = cv2.resize(img,(0,0),None,0.25,0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
 
    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS,facesCurFrame)
 
    #find matches between encodings and known faces
    for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
    #one by one from currentframe 
        matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
        print(faceDis)
        matchIndex = np.argmin(faceDis)
 
        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            print(name)
            y1,x2,y2,x1 = faceLoc
            y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4 #to get the original size of the image as we had scaled it down before 
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            markAttendance(name)
    
    cv2.imshow('Webcam',img)
    cv2.waitKey(1)