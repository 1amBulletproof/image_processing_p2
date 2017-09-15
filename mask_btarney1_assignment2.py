#!/usr/local/bin/python2

# @Author: Brandon Tarney
# @Date: 10/2017

# Program Summary: 
## Allow user to mask an image and then convert all unmasked img-area to black & white
### User presses 'r' to show an img after they have created a mask
### User presses 's' when img is showing to save img as "output_file.jpg"
### User presses '<esc>' to stop showing an image

#Usage: <program> <image_path> 

#TODO:
## 2. Handle user pressing "r" - turn img black & white
## 3. Handle user creating a mask
## 4. Color img black and white EXCEPT user masks 
## 5. Create "marker" on cursor to create the mask?
## 6. Change size of "marker" by pressing "+" and "-"
## 7. Submit zip file w/ images & src code:w

import sys
import cv2

def usage():
        print("USAGE: python2 %s <image_path>" % (sys.argv[0]))
        print(" User presses 'r' to show an img after they have created a mask")
        print(" User presses 's' when img is showing to save img as 'output_file.jpg'")
        print(" User presses '<esc>' to stop showing an image")

def handle_keyboard_input(key, img):
    # wait for '<esc>' key to exit
    if key == 27:    
        cv2.destroyAllWindows()

    # wait for 's' key to save and exit
    elif key == ord('s'):
        cv2.imwrite('output_file.jpg', img)
        cv2.destroyAllWindows()

    #key is 'r', time to present a black & white img
    elif key == ord('r'):
        #Change image color
        grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.destroyAllWindows()
        key2 = show_image(grayImg, 'Black & White Img')
        handle_keyboard_input(key2, grayImg)


def show_image(img, description):
    cv2.imshow(description, img)
    key = cv2.waitKey(7000)
    return key


def main():
    #------------------------------------------------
    #Check and Read arguments
    #------------------------------------------------
    if len(sys.argv) != 2:
        print "ERROR: Missing Arguments"
        usage()
        sys.exit(1)
    elif sys.argv[1] == "-h":
        usage()
        sys.exit(0)
    else:
        input_image = sys.argv[1]

    #------------------------------------------------
    #Read/load image:
    #------------------------------------------------
    #(grayscale img load)
    #img = cv2.imread(sys.argv[1],0)
    #(color img load)
    img = cv2.imread(sys.argv[1],1)
    
    #------------------------------------------------
    #Show OG image (sanity check):
    #------------------------------------------------
    key = show_image(img, 'Input Image')
    handle_keyboard_input(key, img)

    #------------------------------------------------
    #Process Image (showing after each processing)
    #------------------------------------------------

    #------------------------------------------------
    #Show Final Image (with changes):
    #------------------------------------------------
    #Show image and wait: '<esc>' to quit or 's' to save
    #key = show_image(img, 'Final Img')
    #handle_keyboard_input(key, img)


if __name__ == "__main__":
        main()
