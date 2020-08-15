import numpy as np
import cv2
from scipy import ndimage as ndi
def color_seperate(image):
    lower_bgr = np.array([5, 7, 63])          #设定bgr下限
    upper_bgr = np.array([30, 50, 155])        #设定bgr上 限
    mask = cv2.inRange(image, lowerb=lower_bgr, upperb=upper_bgr)  #依据设定的上下限对目标图像进行二值化转换
    cv2.imshow("0", mask)
    kernel1=np.uint8(np.zeros((6,6)))
    for x in range(5):
        kernel1[x,2]=1
        kernel1[2,x]=1

    kernel=np.uint8(np.zeros((3,3)))
    for x in range(3):
        kernel[x,1]=1;
        kernel[1,x]=1;
    #膨胀图像
    dilated = cv2.dilate(mask,kernel1)
    #腐蚀图像
    eroded=cv2.erode(dilated,kernel);

    mask = eroded
    dst = cv2.bitwise_and(image, image, mask=mask) #将二值化图像与原图进行“与”操作；实际是提取前两个frame 的“与”结果，然后输出mask 为1的部分
    dst = mask.astype(np.uint8)
    return dst


def threshold_demo(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # ret, binary = cv2.threshold(gray,0,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    # ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_TRIANGLE)
    # ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_TRUNC)
    ret, binary = cv2.threshold(gray, 150, 250, cv2.THRESH_BINARY)
    print("阈值：", ret)
    # cv2.imshow("binary", binary)
    return binary



if __name__ == '__main__':
    img = cv2.imread("./cotton.png")
    cv2.imshow("1",img)
    # img2 = color_seperate(img)
    img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imshow("2",img2)

    cv2.waitKey(0)

#
# import cv2
# img= cv2.imread('./timg2.jpg')                   #定义图片位置
# # img= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   #转化为灰度图
# def onmouse(event, x, y, flags, param):      #标准鼠标交互函数
#     if event==cv2.EVENT_MOUSEMOVE:           #当鼠标移动时
#         print(img[y,x])                      #显示鼠标所在像素的数值，注意像素表示方法和坐标位置的不同
# def main():
#     cv2.namedWindow("img")                   #构建窗口
#     cv2.setMouseCallback("img", onmouse)     #回调绑定窗口
#     while True:                              #无限循环
#         cv2.imshow("img",img)                #显示图像
#         if cv2.waitKey() == ord('q'):break   #按下‘q’键，退出
#     cv2.destroyAllWindows()                  #关闭窗口
# if __name__ == '__main__':                   #运行
#     main()




# def contrast_brightness_demo(image, c, b):  #其中c为对比度，b为每个像素加上的值（调节亮度）
#     blank = np.zeros(image.shape, image.dtype)   #创建一张与原图像大小及通道数都相同的黑色图像
#     dst = cv2.addWeighted(image, c, blank, 1-c, b) #c为加权值，b为每个像素所加的像素值
#     ret, dst = cv2.threshold(dst, 25, 255, cv2.THRESH_BINARY)
#     return dst
#
#
# capture = cv2.VideoCapture("C:\\Users\\yurunyang\Videos\\cotton.avi")
# redThre = 105
# saturationTh = 42
# while(True):
#     ret, frame = capture.read()
#     cv2.imshow("frame", frame)
#     B = frame[:, :, 0]
#     G = frame[:, :, 1]
#     R = frame[:, :, 2]
#     minValue = np.array(np.where(R <= G, np.where(G <= B, R, np.where(R <= B, R, B)), np.where(G <= B, G, B)))
#     S = 1 - 3.0 * minValue / (R + G + B + 1)
#     fireImg = np.array(np.where(R > redThre, np.where(R >= G, np.where(G >= B, np.where(S >= 0.2, np.where(S >= (255 - R)*saturationTh/redThre, 255, 0), 0), 0), 0), 0))
#     gray_fireImg = np.zeros([fireImg.shape[0], fireImg.shape[1], 1], np.uint8)
#     gray_fireImg[:, :, 0] = fireImg
#     gray_fireImg = cv2.GaussianBlur(gray_fireImg, (7, 7), 0)
#     gray_fireImg = contrast_brightness_demo(gray_fireImg, 5.0, 25)
#     kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
#     gray_fireImg = cv2.morphologyEx(gray_fireImg, cv2.MORPH_CLOSE, kernel)
#     dst = cv2.bitwise_and(frame, frame, mask=gray_fireImg)
#     cv2.imshow("fire", dst)
#     cv2.imshow("gray_fireImg", gray_fireImg)
#     c = cv2.waitKey(40)
#     if c == 27:
#         break