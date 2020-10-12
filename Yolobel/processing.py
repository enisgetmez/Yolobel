import cv2
import numpy as np
from yolobel import vidbox
from yolobel import enums
def video_proc(input_vid):
    tracker = cv2.TrackerKCF_create()
    video = cv2.VideoCapture(input_vid)
    process = False
    while True:
        try:
            if(process== False):
                k,frame = video.read()
                cv2.imshow("Tracking",frame)
                k = cv2.waitKey(30) & 0xff
                if (k == 27):
                    rectangle = cv2.selectROI(frame, False)
                    ok = tracker.init(frame, rectangle)
                    cv2.destroyWindow("ROI selector")
                    process = True
            else:
                ok, frame = video.read()
                ok, rectangle = tracker.update(frame)
                if ok:
                    w,h = np.size(frame, 0),np.size(frame, 1)
                    point1 = (int(rectangle[0]), int(rectangle[1]))
                    point2 = (int(rectangle[0] + rectangle[2]),
                          int(rectangle[1] + rectangle[3]))
                    vidbox.save_out(vidbox.yolo_calculator(point1,point2,w,h,rectangle),frame)
                    cv2.rectangle(frame, point1, point2, (0,0,255), 2, 2)
                    

                cv2.imshow("Tracking", frame)
                k = cv2.waitKey(1) & 0xff
                if k == 27 : break
        except:
             cv2.destroyAllWindows()
             break