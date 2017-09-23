#!/usr/local/bin/python2

# @Author: Brandon Tarney
# @Date: 10/2017
# @see: https://github.com/opencv/opencv/blob/master/samples/python/inpaint.py

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
import numpy as np
from masker import Masker


def usage():
        print("\nUSAGE: python2 %s <image_path>" % (sys.argv[0]))
        print(" User presses ' ' (space) to display an img after they have created a mask")
        print(" User presses 'r' to reset an img while editing its mask")
        print(" User presses 's' when img is showing to save img as 'output_file.jpg'")
        print(" User presses 'q' at any time to quit\n")


def color_function():
    white_mark = (255,255,255)
    white_mask_value = 255
    return white_mark, white_mask_value


def show_image(img, description, duration_ms=-1):
    cv2.imshow(description, img)
    if(duration_ms == -1):
        key = cv2.waitKey()
    else:
        key = cv2.waitKey(duration_ms)
    return key


def handle_keyboard_input(key, img):
    # wait for 's' key to save and exit
    if key == ord('s'):
        print("Saving file to output_file.jpg")
        cv2.imwrite('output_file.jpg', img)
        cv2.destroyAllWindows()
    else:
        cv2.destroyAllWindows()


def main():
    #------------------------------------------------
    #Check and Read arguments
    #------------------------------------------------
    usage()
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
    img = cv2.imread(sys.argv[1],1)

    if img is None:
        print("Could not load image, quitting...")
        usage()
        sys.exit(1)

    #------------------------------------------------
    #Setup Image Processing (showing after each processing)
    #------------------------------------------------
    img_clone = img.copy()
    final_img = img.copy()

    #Setup the mask
    mask = np.zeros(img.shape[:2], np.uint8)

    #The eventual background image
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_gray = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2BGR)

    images = [img_clone, mask]

    #Allow user to markup img (creating the mask)
    masker = Masker("Create Mask", images, color_function)

    #------------------------------------------------
    #Process Image (showing after each processing)
    #------------------------------------------------
    while True:
        key = cv2.waitKey()
        if key == ord('+'):
            masker.increase_thickness(10)
        elif key == ord('-'):
            masker.decrease_thickness(10)
        if key == ord('q'):
            print("User pressed 'q' to quit")
            sys.exit(1)
        if key == ord('r'):
            img_clone[:] = img
            mask[:] = 0
            masker.show()
        if key == ord(' '):
            mask_inv = cv2.bitwise_not(mask)
            print("Showing Masked Image")
            key = show_image(img_clone, 'img_marked', -1)
            handle_keyboard_input(key, img_clone)
            print("Showing Background Image")
            bg_img = cv2.bitwise_and(img_gray, img_gray, mask = mask_inv)
            key = show_image(bg_img, 'BG IMG', -1)
            handle_keyboard_input(key, bg_img)
            print("Showing Foreground Image")
            fg_img = cv2.bitwise_and(img, img, mask = mask)
            key = show_image(fg_img, 'FG IMG', -1)
            handle_keyboard_input(key, fg_img)
            final_img = cv2.add(bg_img, fg_img)
            break

    #------------------------------------------------
    #Show Final Image (with changes):
    #------------------------------------------------
    print("Showing Final Image")
    key = show_image(final_img, 'Showing the Final Image (combination of the bg and fg img)')
    handle_keyboard_input(key, final_img)



if __name__ == "__main__":
        main()
