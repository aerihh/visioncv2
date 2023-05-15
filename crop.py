import os
import cv2

output_dir = "C:/Users/Irving/Documents/Vision/crops"
mask = cv2.imread("C:/Users/Irving/Documents/Vision/mascarav3.png", 0)

analysis = cv2.connectedComponentsWithStats(mask, 4, cv2.CV_32S)

(totalLabels, label_ids, values, centroid) = analysis

slots = []

for i in range(1, totalLabels):

    area = values[i, cv2.CC_STAT_AREA]

    x1 = values[i, cv2.CC_STAT_LEFT]
    y1 = values[i, cv2.CC_STAT_TOP]
    w = values[i, cv2.CC_STAT_WIDTH]
    h = values[i, cv2.CC_STAT_HEIGHT]

    pt1 = (x1,y1)
    pt2 = (x1 + w, y1 + h)
    (X, Y) = centroid[i] 

    slots.append([x1, y1, w, h])



video_path = "D:/video/parking_3.avi"

cap = cv2.VideoCapture(video_path)

frame_nmr = 0
cap.set(cv2.CAP_PROP_POS_FRAMES, frame_nmr)
ret, frame = cap.read()

while ret:
    
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_nmr)
    ret, frame = cap.read()

    if ret:
        #slot_nmr es el el cajon y slot son los puntos en este caso, una lista conformada por 4 listas, es decir [[1],[2],[3],[4]]
        #no se puede iterar por que 
        for slot_nmr, slot in enumerate(slots):
            print(len(slots))
            
            if slot_nmr in [0,1,2,3,4,5,6,7,8,9,10,11,12]:
                
                #slot = frame[int(slot[1]):int(slot[1]) + int(slot[3]), int(slot[0]):int(slot[0]) + int(slot[2]), :]
                slot = frame[slot[1]:slot[1] + slot[3], slot[0]:slot[0] + slot[2], :]
                print(slot)

                #slot += 1
                cv2.imwrite(os.path.join(output_dir, '{}_{}.jpg'.format(str(frame_nmr).zfill(5), str(slot_nmr).zfill(5))), slot)

        frame_nmr += 8

cap.release()