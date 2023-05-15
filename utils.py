import pickle

from skimage.transform import resize
import numpy as np
import cv2


EMPTY = True
NOT_EMPTY = False

MODEL = pickle.load(open("model.p", "rb"))

def empty_or_not(spot_bgr):

    flat_data = []

    img_resized = resize(spot_bgr, (15,15,3))
    flat_data.append(img_resized.flatten())
    flat_data = np.array(flat_data)

    y_output = MODEL.predict(flat_data)

    if y_output == 0:
        return EMPTY
    else:
        return NOT_EMPTY
    

 