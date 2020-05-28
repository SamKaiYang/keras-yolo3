import os
import cv2 as cv
print("當下位置：", os.getcwd())
print("當下位置所有的檔案：", os.listdir(os.getcwd()))

path = os.getcwd() + "/JPG4"

new_folder = "Resize_Defect4"

#print(len(os.listdir(path)))
'''
for i in range(len()):
	print(i)
	img = cv.imread(text+str(i)+".jpg", 1)
	resize_img = cv.resize(img, (416, 416))
	cv.imwrite("resize_"+text+str(i)+".jpg", resize_img)

cv.destroyAllWindows()
'''

if not os.path.exists(os.getcwd()+"/"+new_folder):
	    os.makedirs(new_folder)

num = 1

for i in sorted(os.listdir(path)):
	print(i)
	img = cv.imread(path+"/"+i, 1)
	#cv.imshow("image", img)
	resize_img = cv.resize(img, (416, 416))
	cv.imwrite(new_folder+"/"+"Defect"+str(num)+".jpg", resize_img)
	num = num + 1

cv.destroyAllWindows()
