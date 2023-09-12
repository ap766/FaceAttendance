# FaceAttendance
## About
Basically, the app detects your face and marks your attendance by putting ur name beside the time of attendance into an csv file
## Tech Stack
+ Python (opencv , face_recognisation, os )
## Machine Learning
+ First we convert images to rgb form
+ Second we encode the images (basically find different metrics like distance from eyes to nose , nose to lips ,size of nose etc)
+ Third , we compare the image taken by web cam to the original images in our folder.
We are making use of a trained neural network(through facial recognisation library) which helps us find the encodings and we SVM Classifier to compare images.
## OUTPUTS

## How to run?
Put images in the FaceAttendanceFolder in the format of <name>.png and run python AttendanceProject.py .
