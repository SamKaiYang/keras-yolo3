import cv2 as cv
import numpy as np
import argparse
dl = cv.getStructuringElement(cv.MORPH_ELLIPSE, (3, 3))
# 构建参数解析器
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv.imread(args["image"])
BG_th = cv.threshold(image.copy(), 128, 255, cv.THRESH_BINARY)[1]


bitwiseAnd = cv.bitwise_and(image-BG_th, image)

cv.imshow("Image", image)
cv.imshow("BG_th", bitwiseAnd)
cv.waitKey(0)
'''
# 创建矩形区域，填充白色255
rectangle = np.zeros(image.shape[0:2], dtype = "uint8")
cv.rectangle(rectangle, (25, 25), (275, 275), 255, -1)
cv.imshow("Rectangle", rectangle)
 
# 创建圆形区域，填充白色255
circle = np.zeros(image.shape[0:2], dtype = "uint8")
cv.circle(circle, (150, 150), 150, 255, -1)
cv.imshow("Circle", circle)

# 在此例（二值图像）中，以下的0表示黑色像素值0, 1表示白色像素值255
# 位与运算，与常识相同，有0则为0, 均无0则为1
bitwiseAnd = cv.bitwise_and(rectangle, circle)
cv.imshow("AND", bitwiseAnd)
cv.waitKey(0)
 
# 或运算，有1则为1, 全为0则为0
bitwiseOr = cv.bitwise_or(rectangle, circle)
cv.imshow("OR", bitwiseOr)
cv.waitKey(0)

# 非运算，非0为1, 非1为0
bitwiseNot = cv.bitwise_not(circle)
cv.imshow("NOT", bitwiseNot)
cv.waitKey(0) 

# 异或运算，不同为1, 相同为0
bitwiseXor = cv.bitwise_xor(rectangle, circle)
cv.imshow("XOR", bitwiseXor)
cv.waitKey(0)
'''
cv.destroyAllWindows()
