import cv2 as cv
import os


path = os.getcwd()
print("當下位置所：", path)
print("當下位置所有的檔案：", os.listdir(path))

for i in sorted(os.listdir(path)):

	img = cv.imread(path+"/"+i, 1)
	cv.imshow("Image"+i, img)
	cv.waitKey(0)
	cv.destroyAllWindows()


