#!/usr/local/bin/python2

#handle mouse input

class MouseHandler:

    def __init__(self, img, mask, color):
        self.img = img
        self.mask = mask
        self.color = color
        self.previous_pt = None

    def show_img(self):

    def update_img(self):
        #update img

        #display updated img
        cv2.destroyAllWindows()
        self.show_img()

    def update_mask(self):

    def handle_mouse_event(self, event, x, y, flags, param):
        tmp_pt = (x,y)
        print("General Mouse Event!")

        if event == cv2.EVENT_LBUTTONDOWN:
            self.previous_pt = tmp_pt
        elif event == cv2.EVENT_LBUTTONUP:
            self.last_pt
        elif event == cv2.EVENT_LBUTTONDOWN:
        elif flags & cv2.EVENT_FLAG_LBUTTON:

