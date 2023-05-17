import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

from utils import empty_or_not
#from skimage.transform import resize

photo = "C:/Users\Irving/Documents/Vision/test_imgs"
mask = cv2.imread("C:/Users/Irving/Pictures/Saved Pictures/maskv5.png", 0)
cap = cv2.VideoCapture("C:/Users/Irving/Pictures/Camera Roll/WIN_20230426_18_44_22_Pro.mp4")
cam = cv2.VideoCapture(0)

#print(np.ndarray(cam))

connected_components = cv2.connectedComponentsWithStats(mask, 4, cv2.CV_32S)

slots = []

(totalLabels, label_ids, values, centroid) = connected_components

coef = 1
for i in range(1, totalLabels):

    # Now extract the coordinate points
    x1 = int(values[i, cv2.CC_STAT_LEFT] * coef)
    y1 = int(values[i, cv2.CC_STAT_TOP] * coef)
    w = int(values[i, cv2.CC_STAT_WIDTH] * coef)
    h = int(values[i, cv2.CC_STAT_HEIGHT] * coef)

    slots.append([x1, y1, w, h])

def Box():
    for i, spot in enumerate(slots):
        x1, y1, w, h = spot

        imgCrop = frame[y1:y1 + h, x1:x1 + w]       

        #cv2.imshow(f'spot: {i}',imgCrop)

ret = True
frameRate = 0 #frame rate
cam.set(cv2.CAP_PROP_POS_FRAMES, frameRate)
ret, frame = cam.read()

height, width = cam.get(cv2.CAP_PROP_FRAME_HEIGHT), cam.get(cv2.CAP_PROP_FRAME_WIDTH)

#print(height,width)

#filename = "C:/Users/Irving/Pictures/parklot.jpg"
#cv2.imwrite(filename, frame)

while ret:

    cam.set(cv2.CAP_PROP_POS_FRAMES, frameRate)
    #CONDITION TO LOOP VIDEO
    #if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
    #    cap.set(cv2.CAP_PROP_POS_FRAMES,0)
    ret, frame = cam.read()

    Box()

    resized_frame = cv2.resize(frame, (int(height), int(width)), interpolation = cv2.INTER_AREA)

    for slot in slots:
        x1, y1, w, h = slot

        slotCrop = frame[y1:y1 + h, x1:x1 + w, :]

        slotStatus = empty_or_not(slotCrop)

        if slotStatus:
            frame = cv2.rectangle(frame,(x1, y1), (x1 + w, y1 + h), (0, 255, 0), 2)
            #vacio
        else:
            frame = cv2.rectangle(frame,(x1, y1), (x1 + w, y1 + h), (0, 0, 255), 2)
            #ocupado
    #if ret:
    #    filename = photo + "/image_" +  str(int(frameRate)) + ".jpg"
    #    cv2.imwrite(filename, frame)
    #    frameRate += 8

    cv2.imshow('Spots', frame)

    if cv2.waitKey(10) & 0xFF == 27:
        break

cam.release()
cv2.destroyAllWindows()


