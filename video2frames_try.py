# from convenience import is_cv3
import cv2
import imutils
from imutils import is_cv3

def count_frames(path, override=False):
    
    # grab a pointer to the video file and initialize the total
    # number of frames read
    video = cv2.VideoCapture(path)
    total = 0
    # if the override flag is passed in, revert to the manual
    # method of counting frames
    if override:
        total = count_frames_manual(video)
    print(total)
    
    
    
    video = cv2.VideoCapture(path)
    if (video.isOpened() == False):
        print("Error reading video file")
    success = True
    count = 1
    while success:
        success, frame = video.read()
        print(success)
        name = "/home/tcestudent/integration/extracted_frames/" + str(count)+".jpg"
        if success==True:
            cv2.imwrite(name,frame)
            print("Frame {} Extracted Successfully".format(count))
            count += 1
        else:
            break
        
        
count_frames("/home/tcestudent/integration/sakura.mp4")
