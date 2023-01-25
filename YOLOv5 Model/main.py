from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.filemanager import MDFileManager
from kivy.uix.boxlayout import BoxLayout

from kivymd.toast import toast

from plyer import filechooser
from kivy.uix.button import Button
from kivy.properties import ListProperty
from kivy.app import App
from textwrap import dedent
from os import startfile

import cv2
import os
from PIL import Image
import time
#import torch
import numpy as np


from fordetectingandkivy import *

############################################################


# , force_reload=True
# model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5/runs/train/exp/weights/best.pt')

############################################################

Window.maximize()


KV = '''
WindowManager:
    First:
    Second:
    Third:
    Fourth:
    Fifth:
<First>:
    name: 'First'

    ScreenWallpaper:
        size :320,500
        AsyncImage:
            allow_stretch: True
            keep_ratio:False
            source:'https://ecommerce-platforms.com/wp-content/uploads/2014/04/12-free-blurred-backgrounds.jpg'
            
    MDLabel:
        text:'Object detection'
        font_style: 'Button'
        font_size: 50
        halign: "center"
        size_hint_y: None
        pos_hint: {"center_x":.5,"center_y":.8}
        padding_y: 10        
        opposite_colors:True
        text_color:self.specific_text_color
        theme_text_color:"Custom"
   
    MDRoundFlatButton:
        text:'Click here to start the app'
        font_style: 'Button'
        font_size: 22
        halign: "left"
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1
        pos_hint: {"center_x":.5,"center_y":.3}
        on_press:
            root.manager.current = 'second'
            root.manager.transition.direction = 'left'

<Second>:
    name: 'second'
    ScreenWallpaper:
        size :320,500
        AsyncImage:
            allow_stretch: True
            keep_ratio:False
            source:'https://ecommerce-platforms.com/wp-content/uploads/2014/04/12-free-blurred-backgrounds.jpg'
     

    MDRoundFlatButton:
        text:'Web-Cam'
        font_style: 'Button'
        font_size: 28
        halign: "left"
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1
        pos_hint: {"center_x":.5,"center_y":.7}
        on_press:
            # root.manager.current = 'third'
            # root.manager.transition.direction = 'left'
            root.capture_video()


    MDRoundFlatButton:
        text:'Upload Image'
        font_style: 'Button'
        font_size: 28
        halign: "left"
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1
        pos_hint: {"center_x":.5,"center_y":.5}
        on_press:
            root.manager.current = 'fourth'
            root.manager.transition.direction = 'left'

    MDRoundFlatButton:
        text:'Upload Video'
        font_style: 'Button'
        font_size: 28
        halign: "left"
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1
        pos_hint: {"center_x":.5,"center_y":.3}
        on_press:
            root.manager.current = 'fifth'
            root.manager.transition.direction = 'left'
<Third>:
    name :'third'

    ScreenWallpaper:
        size :320,500
        AsyncImage:
            allow_stretch: True
            keep_ratio:False
            source:'https://ecommerce-platforms.com/wp-content/uploads/2014/04/12-free-blurred-backgrounds.jpg'
    MDCard: #card to hold components
        orientation: "vertical"
        padding: "10dp"
        spacing: "5dp"
        pos_hint: {"center_x":0.5,"center_y":0.68}
        md_bg_color: rgba(200,200,210,255)
        radius:(20,20,20,20)
        size_hint: 0.6,0.6
        elevation: 6
        CameraClick:
            orientation: 'vertical'
            Camera:
                id: camera
                resolution: (640,480)
                play: False


    MDRoundFlatButton:
        text:'Play'
        font_style: 'Button'
        font_size: "15dp"
        size_hint:0.10,0.05
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1
        pos_hint: {"center_x":.3,"center_y":.2}
        on_press:camera.play = not camera.play
        # on_press: root.capture()

    MDRoundFlatButton:
        text:'Capture'
        font_style: 'Button'
        font_size: "15dp"
        size_hint:0.10,0.05
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1
        pos_hint: {"center_x":.5,"center_y":.2}
        on_press:camera.play = not camera.play

    MDRoundFlatButton:
        text:'Blur'
        font_style: 'Button'
        font_size: "15dp"
        size_hint:0.10,0.05
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1
        pos_hint: {"center_x":.7,"center_y":.2}
        on_release: root.blur_img()

    MDRoundFlatButton:
        text:'Back'
        font_style: 'Button'
        font_size: "15dp"
        size_hint:0.10,0.05
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1
        pos_hint: {"center_x":.5,"center_y":.1}
        on_press:
            root.manager.current = 'second'
            root.manager.transition.direction = 'left'


<Fourth>:
    name:"fourth"
    ScreenWallpaper:
        size :320,500
        AsyncImage:
            allow_stretch: True
            keep_ratio:False
            source:'https://ecommerce-platforms.com/wp-content/uploads/2014/04/12-free-blurred-backgrounds.jpg'
            
    Screen:
        size:root.height,root.width
        MDRoundFlatIconButton:
            text: "Select Image"
            icon: "folder"
            font_style: 'Button'
            font_size: "15dp"
            size_hint:0.10,0.05
            theme_text_color: "Custom"
            text_color: 0, 0, 0, 1
            pos_hint: {'center_x': .22, 'center_y': .2}
            on_release: root.file_manager_open()

        Image:
            id:image
            source: 'photo.png'
            pos_hint: {'center_x': .22, 'center_y': .6}
            size_hint: None,None
            size: 280,280

        MDRoundFlatButton:
            text:'Blur'
            font_style: 'Button'
            font_size: "15dp"
            size_hint:0.10,0.05
            theme_text_color: "Custom"
            text_color: 0, 0, 0, 1
            pos_hint: {"center_x":.49,"center_y":.65}
            on_release: root.output_blur()

        Image:
            id:newimage
            source: ''
            pos_hint: {'center_x': .77, 'center_y': .6}
            size_hint: None,None
            size: 280,280

        MDRoundFlatButton:
            text:'Back'
            font_style: 'Button'
            font_size: "15dp"
            size_hint:0.10,0.05
            theme_text_color: "Custom"
            text_color: 0, 0, 0, 1
            pos_hint: {"center_x":.49,"center_y":.1}
            on_press:
                root.manager.current = 'second'
                root.manager.transition.direction = 'left'
    
<Fifth>:
    name:"fifth"
    ScreenWallpaper:
        size :320,500
        AsyncImage:
            allow_stretch: True
            keep_ratio:False
            source:'https://ecommerce-platforms.com/wp-content/uploads/2014/04/12-free-blurred-backgrounds.jpg'
    Screen:
        size:root.height,root.width
        MDRoundFlatIconButton:
            text: "Select Video"
            icon: "folder"
            font_style: 'Button'
            font_size: "15dp"
            size_hint:0.10,0.05
            theme_text_color: "Custom"
            text_color: 0, 0, 0, 1
            pos_hint: {'center_x': .22, 'center_y': .2}
            on_release: root.file_manager_open()

        MDLabel:
            id:txt
            text:""
            halign: "center"
            pos_hint: {"center_x":.22, "center_y":.6}

        MDRoundFlatButton:
            text:'Video Blur'
            font_style: 'Button'
            font_size: "15dp"
            size_hint:0.10,0.05
            theme_text_color: "Custom"
            text_color: 0, 0, 0, 1
            pos_hint: {"center_x":.49,"center_y":.65}
            on_release: root.output_videoblur()

        MDRoundFlatButton:
            text:'Back'
            font_style: 'Button'
            font_size: "15dp"
            size_hint:0.10,0.05
            theme_text_color: "Custom"
            text_color: 0, 0, 0, 1
            pos_hint: {"center_x":.49,"center_y":.1}
            on_press:
                root.manager.current = 'second'
                root.manager.transition.direction = 'left'
'''

class FileChoose(Button):
    pass

        
pic_path=''
class First(Screen):
    pass
class Second(Screen):


    def capture_video(self):
        
        # vid = cv2.VideoCapture(0)
        # while(True):

        source_of_image(str(0))

    pass 
        


        #     # Capture the video frame
        #     # by frame
        #     ret, frame = vid.read()

        #     # Make detections 
        #     results = model(frame)
        #     ksize = (10, 10)

        #     # Display the resulting frame
        #     cv2.imshow('frame', np.squeeze(results.render()))

        #     # the 'q' button is set as the
        #     # quitting button you may use any
        #     # desired button of your choice
        #     if cv2.waitKey(1) & 0xFF == ord('q'):
        #         break


        # # After the loop release the cap object
        # vid.release()
        # # Destroy all the windows
        # cv2.destroyAllWindows()
    

class Third(Screen):
    pass
class Fourth(Screen):
    global pic_path
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            #preview=True
        )
        self.rot_count=0
    

    def file_manager_open(self):
        PATH ="/"
        self.file_manager.show(PATH)  # output manager to the screen
        self.manager_open = True
    
    def select_path(self, path):
        global pic_path
        '''It will be called when you click on the file name
        or the catalog selection button.

        :type path: str;
        :param path: path to the selected directory or file;
        '''
        print(path)
        pic_path=path
        self.ids.image.source = path
        self.exit_manager()

    def exit_manager(self, *args):
        '''Called when the user reaches the root of the directory tree.'''

        self.manager_open = False
        self.file_manager.close()


    def output_blur(self):
        global pic_path
        if pic_path == '':
            pass
        else:
            source_of_image(pic_path)
            detectedimg=output_of_detected_image(pic_path)
            # detectedimg= cv2.cvtColor(detectedimg, cv2.COLOR_BGR2RGB)
            cv2.imwrite('yyyyy.jpg',detectedimg)
            self.ids.newimage.source = str(detectedimg)
            # self.ids.newimage.source = x

        




            # results = model(pic_path)
            # # results.print()
            # detectedimg= np.squeeze(results.render())
            # detectedimg= cv2.cvtColor(detectedimg, cv2.COLOR_BGR2RGB)
            # cv2.imwrite('new.jpg',detectedimg)
            # self.ids.newimage.source = 'new.jpg'

class Fifth(Screen):
    global vid_path
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            #preview=True
        )
        self.rot_count=0
    

    def file_manager_open(self):
        PATH ="/"
        self.file_manager.show(PATH)  # output manager to the screen
        self.manager_open = True
    
    def select_path(self, path):
        global vid_path
        '''It will be called when you click on the file name
        or the catalog selection button.

        :type path: str;
        :param path: path to the selected directory or file;
        '''
        print(path)
        vid_path=path
        self.ids.txt.text=path
        self.exit_manager()

    def exit_manager(self, *args):
        '''Called when the user reaches the root of the directory tree.'''

        self.manager_open = False
        self.file_manager.close()

    def output_videoblur(self):
        global vid_path
        if vid_path == '':
            pass
        else:
            source_of_image(vid_path)
            detectedvid= output_of_detected_video(vid_path)
            # cv2.imwrite('new',detectedvid)
            
        
            startfile(detectedvid)

            #############################################################
            # vid = cv2.VideoCapture(str(detectedvid))
            # while(True):
            #     # Capture the video frame
            #     # by frame
            #     ret, frame = vid.read()
            #     if ret == True:
            #         cv2.imshow('detect video', frame)
            #         if cv2.waitKey(1) & 0xFF == ord('q'):
            #             break
        
            # vid.release()
            # cv2.destroyAllWindows()
            ###############################################################



class ScreenWallpaper(BoxLayout):
    pass

#Class for Screen Manager
class WindowManager(ScreenManager):
    pass


class CameraClick(BoxLayout):
    # def capture(self):
    #     '''
    #     Function to capture the images and give them the names

    #     according to their captured time and date.
    #     '''
    #     # camera = self.ids['camera']
    #     # timestr = time.strftime("%Y%m%d_%H%M%S")
    #     # camera.export_to_png("IMG_" + timestr)
    #     # print("Captured")

    # def capture_video(self):
        
    #     vid = cv2.VideoCapture(0)
    #     while(True):
    #         # Capture the video frame
    #         # by frame
    #         ret, frame = vid.read()

    #         # Make detections 
    #         results = model(frame)
    #         ksize = (10, 10)

    #         # Display the resulting frame
    #         cv2.imshow('frame', np.squeeze(results.render()))

    #         # the 'q' button is set as the
    #         # quitting button you may use any
    #         # desired button of your choice
    #         if cv2.waitKey(1) & 0xFF == ord('q'):
    #             break


    #     # After the loop release the cap object
    #     vid.release()
    #     # Destroy all the windows
    #     cv2.destroyAllWindows()
    pass


class MainApp(MDApp):


    def build(self):
        global sm

        #Adding screens with screen manager
        sm = ScreenManager()
        sm.add_widget(First(name='First'))
        sm.add_widget(Second(name='Second'))
        sm.add_widget(Third(name='third'))
        sm.add_widget(Fourth(name='fourth'))
        sm.add_widget(Fifth(name='fifth'))
        return Builder.load_string(KV)




if __name__ == "__main__":
    MainApp().run()