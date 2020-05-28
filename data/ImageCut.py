import cv2 as cv
import os
path = os.getcwd()

BackGroundImage = "Screw_0.jpg"
SenseFolder = "/Camera_Picture/"
BackGroundImagePath = path + SenseFolder +  BackGroundImage
es = cv.getStructuringElement(cv.MORPH_ELLIPSE, (3, 3))
dl = cv.getStructuringElement(cv.MORPH_ELLIPSE, (3, 3))
BG = cv.imread(BackGroundImagePath, 0)
Image = sorted(os.listdir(path+SenseFolder))

def imshow_with_position(WindowName, position, image):
	cv.namedWindow(WindowName)
	cv.moveWindow(WindowName, position[0], position[1])
	cv.imshow(WindowName, image)

def main():
	for i in Image:
		if i == BackGroundImage:
			continue
		else:
			print(i)
			FP = cv.imread(path + SenseFolder + i,0)
			BG_th = cv.threshold(BG.copy(), 128, 255, cv.THRESH_BINARY)[1]
			FP_th = cv.threshold(FP.copy(), 128, 255, cv.THRESH_BINARY)[1]

			#cv.imshow("BackGround", BG)
			#cv.waitKey(0)
			#cv.imshow("FP_th-BG_th", FP_th-BG_th)

			erosion = cv.erode(FP_th-BG_th, es, iterations = 1)
			
			#imshow_with_position("erosion " + i, (40, 800), erosion)

			dilate = cv.dilate(erosion, dl, iterations=5) # 形态学膨胀

			#imshow_with_position("dilate " + i, (1000, 30), dilate)
			
			image, contours, hierarchy = cv.findContours(dilate, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE) # 该函数计算一幅图像中目标的轮廓

			counter_offset = 0
			'''
			for c in contours:
				print(cv.contourArea(c))

				if cv.contourArea(c) > 1:
					(x, y, w, h) = cv.boundingRect(c)
					cv.rectangle(FP, (x - counter_offset, y - counter_offset), 
					(x + w + counter_offset, y + h + counter_offset), (255, 255, 0), 2)
			'''
			if len(contours) != 0:
				#find max contour
				c = max(contours, key = cv.contourArea)
				(x, y, w, h) = cv.boundingRect(c)
				cv.rectangle(FP, (x - counter_offset, y - counter_offset), (x + w + counter_offset, y + h + counter_offset), (255, 255, 0), 2)
				print("X_Min: ", x, " Y_Min: ", y, " X_Max: ", x+w, " Y_Max: ", y+h)
			imshow_with_position("Cut" + i, (1000, 800), FP)
			cv.waitKey(0)
			cv.destroyAllWindows()

if __name__=="__main__":
	main()

