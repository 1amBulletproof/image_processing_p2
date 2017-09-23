#!/usr/local/bin/python2

# @Author: Brandon Tarney
# @Date: 10/2017
# @see: https://github.com/opencv/opencv/blob/master/samples/python/common.py

# Class Summary:
## Create and track a Mask imposed on another image
### image appears as though the user is painting on the image


import cv2


class Masker:
    def __init__(self, windowname, images, colors_func):
        self.prev_pt = None
        self.windowname = windowname
        self.images = images
        self.colors_func = colors_func
        self.dirty = False
        self.thickness = 25 #default is 5
        self.show()
        cv2.setMouseCallback(self.windowname, self.on_mouse)
        #print("masker init")

    def increase_thickness(self, increase):
        if self.thickness <= 200:
            self.thickness = self.thickness + increase
        print("Line Thickness = " + str(self.thickness))

    def decrease_thickness(self, decrease):
        if self.thickness >= 10:
            self.thickness = self.thickness - decrease
        print("Line Thickness = " + str(self.thickness))

    def show(self):
        # print("Mask: SHOW()")
        cv2.imshow(self.windowname, self.images[0])

    def on_mouse(self, event, x, y, flags, param):
        pt = (x, y)
        #print("General Mouse Event!")
        if event == cv2.EVENT_LBUTTONDOWN:
            self.prev_pt = pt
        #    print("Left Button Down")
        elif event == cv2.EVENT_LBUTTONUP:
            self.prev_pt = None
        #    print("Left Button Up")

        if self.prev_pt and flags & cv2.EVENT_FLAG_LBUTTON:
            '''
            # Logic: literally draw lines on the img displayed while also creating the mask where the lines exist in the image
            # 
            # zip creates tuple for each dst[] & each color (the fcn returns 2 things): 
            #   [ (self.images[0] (the img to be marked-up), self.colors_func()[0] (bgr color of mark on img ), 
            #     (self.images[1] (mask: 0's), self.colors_func()[1] ( NON-0 val, the mask))]
            # cv2.line modifies its img parameter
'''
            for dst, color in zip(self.images, self.colors_func()):
                cv2.line(dst, self.prev_pt, pt, color, self.thickness)
            self.dirty = True
            self.prev_pt = pt
        #    print("about to re-show the img")
            self.show()
