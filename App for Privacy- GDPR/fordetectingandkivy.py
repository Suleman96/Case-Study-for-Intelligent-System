from yolov7_object_blurring.un_detect_and_blur import *
# from detect_and_blur import *

import cv2
import math
import numpy as np
import os
import time

# 'C:/Users/virtu/Desktop/Drowsiness Detection/'

def source_of_image(path_of_image):
    # if path_of_image == str(0):
    #     run(source= path_of_image)
    # else:
        # file_name = os.path.basename(path_of_image)
        # source_path =os.path.join('C:/Users/virtu/Desktop/Drowsiness Detection/', file_name)
        # source_path =path_of_image

        # run(source= ROOT/path_of_image )
        # run(source= path_of_image )
    detect(source= path_of_image )

        
    return 

# file ending with .jpg or .mp4 or .jpeg


def output_of_detected_video(path_of_image):
    project= 'runs/detect'
    name='exp'
    file_name = os.path.basename(path_of_image)
    file_name_without_extension, file_extension = os.path.splitext(file_name)

    print(file_name)
    print(file_extension)
    print(file_name_without_extension)

    # if file_extension !=  '.mp4':
    #     print(file_extension)
    #     print(file_name_without_extension)

    #     file_name_without_extension= file_name_without_extension+'.mp4'

    #     directoryofdetectedimage = Path(project) / name/ file_name_without_extension

    #     print(file_extension)
    #     print(file_name_without_extension)

    # else:
    print(file_extension)
    print(file_name_without_extension)

    directoryofdetectedimage = Path(project) / name/ file_name

    print(file_extension)
    print(file_name_without_extension)


    return directoryofdetectedimage

def output_of_detected_image(path_of_image):
    project='runs/detect'
    file_name = os.path.basename(path_of_image)
    name='exp'
    directoryofdetectedimage = Path(project) / name/ file_name

    return directoryofdetectedimage

# image_path = cv2.imread("C:/Users/virtu/Desktop/Drowsiness Detection/20180402113123_NumberPlate_Swift.jpg")
# source_path =os.path.join('C:/Users/virtu/Desktop/Drowsiness Detection/', 'NumberPlate_Swift.jpg')

# print(ROOT,'3')
# run(source= ROOT/source_path )
# print(ROOT,'2')

# project=ROOT / 'runs/predict-seg'
# print(ROOT,'1')
# name='exp'
# directoryofdetectedimage =save_dir = Path(project) / name


# print(x)




# isExist = os.path.exists(source_path)


# if isExist == run(source= ROOT/source_path ):


#     run(Pa)

# if isExist == run(source= ROOT/source_path)


