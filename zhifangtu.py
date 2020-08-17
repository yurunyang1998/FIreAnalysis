import  cv2

def hsv_histogram(image_3chanal):
    import matplotlib.pyplot as plt
    # 按R、G、B三个通道分别计算颜色直方图
    b_hist = cv2.calcHist([image_3chanal], [0], None, [256], [0, 256])
    g_hist = cv2.calcHist([image_3chanal], [1], None, [256], [0, 256])
    r_hist = cv2.calcHist([image_3chanal], [2], None, [256], [0, 256])

    # 显示3个通道的颜色直方图
    plt.plot(b_hist, label='B', color='blue')
    plt.plot(g_hist, label='G', color='green')
    plt.plot(r_hist, label='R', color='red')
    plt.legend(loc='best')
    plt.xlim([0, 256])
    plt.grid()
    plt.show()

if __name__ == '__main__':
    img = cv2.imread("./cotton.png")
    cv2.imshow("1",img)
    # img2 = color_seperate(img)
    hsv_histogram(img)
    # img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # cv2.imshow("2",img2)

    cv2.waitKey(0)
