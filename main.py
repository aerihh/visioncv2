import cv2
import numpy as np

from coordinates import data

video_path = "C:/Users/Irving/Pictures/Camera Roll/WIN_20230426_18_33_27_Pro.mp4"
video_pk = cv2.VideoCapture(video_path)

parking_tec = cv2.imread("C:/Users/Irving/Documents/Vision/PARKING_TEC.png")
mask = cv2.imread("C:/Users/Irving/Documents/Vision/mascarav2.png", 0)

ret, thresh = cv2.threshold(mask,127,255,0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

#THIS SECTION IS RESERVED FOR THE EMPTY OR NOT

#For now we'll be working with an image of the parking lot 
#remember later on to change for the parking lot tape



flag = True

while flag:
    flag, video = video_pk.read()

    cv2.namedWindow("output", cv2.WINDOW_NORMAL)
    cv2.imshow('output', cv2.drawContours(video, contours, -1, (255, 0, 0), 3))
    #cv2.imshow("output", video)

    imS = cv2.resizeWindow("output", (1280, 720))

    if cv2.waitKey(20) & 0xFF == 27:
        break

video_pk.release()
cv2.destroyAllWindows()