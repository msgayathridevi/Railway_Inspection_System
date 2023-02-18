# %autosave 5

import cv2
from matplotlib import pyplot as plt
import numpy as np
import time
import datetime
import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
import easyocr

now = datetime.datetime.now()
def readsignalboard(img_path):
	#img_path = 'sign.png'
    reader = easyocr.Reader(['en'])
    result = reader.readtext(img_path)
        
    speed = result[0][1]
    acc = result[0][2]
    return(speed, acc)

# speed, acc = readsignalboard("/home/tcestudent/integration/yolo_detection/overall_yolotxt/test/images/aug_0_5520.rf.747b8a45353e2b1d30f43447fc296a14.jpg")
# print("speed : " + str(speed) + "\t Acc : " + str(acc) + "      " + str(now.time()))
