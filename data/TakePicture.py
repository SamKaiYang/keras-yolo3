import cv2 as cv
import os
cam = cv.VideoCapture(0)

cv.namedWindow("test")

img_counter = 0
Save_folder = "Camera_Picture"+"/"
Object_name = "Screw"

if not os.path.exists(os.getcwd()+"/"+Save_folder):
	    os.makedirs(Save_folder)

while True:
    ret, frame = cam.read()
    cv.imshow("test", frame)
    if not ret:
        break
    k = cv.waitKey(1)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = Save_folder+Object_name+"_{}.jpg".format(img_counter)
        resize_img = cv.resize(frame, (416,416))
        cv.imwrite(img_name, resize_img)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()

cv.destroyAllWindows()
