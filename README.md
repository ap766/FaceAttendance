# FaceAttendance
## About
Basically, the app detects your face and marks your attendance by putting your name beside the time of attendance in a csv file
## Tech Stack
+ Python (OpenCV , face_recognisation, os )
## Machine Learning
+ First, we convert images to rgb form
+ Second we encode the images (basically find different metrics like distance from eyes to nose, nose to lips, size of nose, etc.)
+ Third, we compare the image taken by webcam to the original images in our folder.
We are using a trained neural network(through the facial recognition library) which helps us find the encodings and we use an SVM Classifier to compare images.
## OUTPUTS
### Faces are different.
![facial recog](https://github.com/ap766/FaceAttendance/assets/79255079/e84edbe5-5470-4573-a84d-1bd99c536a5d)
### Faces are same.
![faces](https://github.com/ap766/FaceAttendance/assets/79255079/3fb7ad46-9276-449e-ad42-dc284bba032b)
### Attendance - detects face with webcam and displays name if present in the folder
![ap](https://github.com/ap766/FaceAttendance/assets/79255079/e69c4cd2-964d-458f-95fc-27ac5a620cfe)
### Keeps track in the CSV file 
![records](https://github.com/ap766/FaceAttendance/assets/79255079/39ded6fb-7276-43f5-bcb5-6b311e57e98d)
## How to run?
Basic.py can be used to get the basic idea of how face recognition works. For the attendance app,
put images in the FaceAttendanceFolder in the format of <name>.png and run python AttendanceProject.py .
