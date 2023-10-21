"""
HSV is typically better for trackin with images. My threshold range needed to be
relativly large to capture the UCLA logo on my shirt, spanning from (70, 60, 60) to (105, 130, 130)

In bright light conditions, I find the bounding box performs better due to my static threshold range.

Upon using a color picker, I find that too bright of a screen performs worse since webcam begins to flare from the light



Getting started source: https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html
Bounding box graphing: https://docs.opencv.org/4.x/dd/d49/tutorial_py_contour_features.html

"""

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()

    color_scheme = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_bound = np.array([70, 60, 60])
    upper_bound = np.array([105, 130, 130])

    mask = cv2.inRange(color_scheme, lower_bound, upper_bound)

    contours, hierarchy = cv2.findContours(mask, 1, 2)

    max_area = 0
    max_contour = 0
    for i in range(len(contours)):
        x,y,w,h = cv2.boundingRect(contours[i])
        if w*h > max_area:
            max_area = w*h
            max_contour = i

    x,y,w,h = cv2.boundingRect(contours[max_contour])
    cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0),2)
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    # masking the image


cap.release()
cv2.destroyAllWindows()
