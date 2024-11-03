import cv2
import numpy as np
import matplotlib.pyplot as plt

cap_right = cv2.VideoCapture(0)
cap_left = cv2.VideoCapture(1)


B = 0 # Distance between two cameras [cm]
f = 0 # Focal length of the cameras [cm]
alpha = 56.6 # Camera field of view in the horizontal direction [degrees]

count = -1


while True:
    count += 1

    ret_right, frame_right = cap_right.read()
    ret_left, frame_left = cap_left.read()

    
    
    if ret_right:
        cv2.imshow('Right', frame_right)
    if ret_left:
        cv2.imshow('Left', frame_left)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()