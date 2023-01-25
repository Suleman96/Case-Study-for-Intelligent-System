import cv2
import math
import numpy as np
import os
import torch
import matplotlib.pyplot as plt
# %matplotlib inline


model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5/runs/train/exp/weights/best.pt', force_reload=True)



def capture_video():

    vid = cv2.VideoCapture(0)
    while(True):

        # Capture the video frame
        # by frame
        ret, frame = vid.read()

        # Make detections 
        results = model(frame)
        ksize = (10, 10)

        # Display the resulting frame
        cv2.imshow('frame', np.squeeze(results.render()))

        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

'''
img= os.path.join('20180402113123_NumberPlate_Swift.jpg')

def capture_image():


    results = model(img)
    # results.print()
    plt.imshow(np.squeeze(results.render()))
    plt.show()
    
'''



# capture_image()
capture_video()