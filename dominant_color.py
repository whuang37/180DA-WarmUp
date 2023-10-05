"""

In changing the surrounding of my non phone object and the brightness of my phone,
I find that my phone is more robust to lighting change as long as the camera refocuses.

Dominant Color Source: https://code.likeagirl.io/finding-dominant-colour-on-an-image-b4e075f98097
"""

import numpy as np
import cv2
from sklearn.cluster import KMeans

COLOR_BOX = (100, 100, 200, 200) #xywh

cap = cv2.VideoCapture(0)

def find_histogram(clt):
    """
    create a histogram with k clusters
    :param: clt
    :return:hist
    """
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins=numLabels)

    hist = hist.astype("float")
    hist /= hist.sum()

    return hist

while(True):
    ret, frame = cap.read()
    color_scheme = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    cropped_frame = frame[COLOR_BOX[0]:COLOR_BOX[0]+COLOR_BOX[2], COLOR_BOX[1]:COLOR_BOX[3],:]
    frame_reshaped = cropped_frame.reshape((cropped_frame.shape[0]*cropped_frame.shape[1], 3)) # represent as row*column, channel
    clf = KMeans(n_clusters=1, n_init="auto")
    clf.fit(frame_reshaped)
    cv2.rectangle(frame, (COLOR_BOX[0], COLOR_BOX[1]), (COLOR_BOX[0]+COLOR_BOX[2], COLOR_BOX[1]+COLOR_BOX[3]), (0,255,0),2)
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
    print(f"Color: {clf.cluster_centers_[0]}")

    # masking the image
cap.release()
cv2.destroyAllWindows()