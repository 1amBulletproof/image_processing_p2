#!/usr/local//bin/python2

#Class to handle keyboard input

class KeyHandler:

    def __init__(self):

    def handle_keyboard_input(key, img):
        # wait for '<esc>' key to exit
        if key == 27:    
            cv2.destroyAllWindows()

        # wait for 's' key to save and exit
        elif key == ord('s'):
            cv2.imwrite('output_file.jpg', img)
            cv2.destroyAllWindows()

        elif key == ord('r'):
            cv2.destroyAllWindows()




        #key is ' ', time to present a black & white img
        elif key == ord(' '):
            #Change image color
            grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            cv2.destroyAllWindows()
            key2 = show_image(grayImg, 'Black & White Img')
            handle_keyboard_input(key2, grayImg)


            print("BG IMG")
            #print(img_marked)
            bg_img = cv2.bitwise_and(gray_color_img, gray_color_img, mask = mask_inv)
            cv2.imshow('BG IMG', bg_img)
            cv2.waitKey()
            print("FG IMG")
            #print(img_marked)
            fg_img = cv2.bitwise_and(img, img, mask = mask)
            cv2.imshow('FG IMG', fg_img)
            cv2.waitKey()
            final_img = cv2.add(bg_img, fg_img)
            cv2.imshow('FINAL PIC', final_img)




    
