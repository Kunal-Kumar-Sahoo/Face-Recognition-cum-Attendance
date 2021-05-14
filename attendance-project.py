import cv2
import numpy as np
import face_recognition
import os

path = "Dataset"
images = []
names = []
myList = os.listdir(path)
print(myList)

imgElon = face_recognition.load_image_file("Basic Images/1.jpg")
imgElon = cv2.cvtColor(imgElon, cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file("Basic Images/2.jpg")
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)