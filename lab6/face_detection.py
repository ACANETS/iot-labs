import cv2
import argparse

#This file contains the code to detect faces in an image using OpenCV.
#Before we get started, we need to know which file we are looking at.

parser = argparse.ArgumentParser(description='Detects faces in an image and reports how many were found.')
parser.add_argument('filename', metavar='fn', type=str, nargs=1, help='The file with faces to be detected.')

args = parser.parse_args()
print('Looking for faces in the file ', args.filename, '\n')

#The classification code is here.
#First, read the image and convert to grayscale.
test1 = cv2.imread(args.filename[0])
test_gray = cv2.cvtColor(test1, cv2.COLOR_BGR2GRAY)

#Then, use the haar cascade classification built-in to OpenCV to detect faces
haar_human = cv2.CascadeClassifier('/home/pi/opencv-3.0.0/data/haarcascades/haarcascade_frontalface_alt.xml')
humanfaces = haar_human.detectMultiScale(test_gray, 1.1, 5)

print('human faces: ', len(humanfaces))

for (x, y, w, h) in humanfaces:
    cv2.rectangle(test1, (x,y), (x+w, y+h), (0, 255, 0), 2)

cv2.imwrite("faces_highlighted.jpg", test1)
