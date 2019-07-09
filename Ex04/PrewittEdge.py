import cv2
import numpy as np
import matplotlib.pyplot as plt
import time

""" 프리윗
"""
class Prewitt:

    def __init__(self):
        ## 수직 마스크
        self.prewittKernelX = np.array([
            [-1, 0, +1],
            [-1, 0, +1],
            [-1, 0, +1]
        ])

        ## 수평마스크
        self.prewittKernelY = np.array([
            [+1, +1, +1],
            [ 0,  0,  0],
            [-1, -1, -1]
        ])
    def prewittOutLine(self):


        imgPath = r"C:\Users\junhyeon.kim\Desktop\AI_STU\imgCollecter\ferrari.jpg"
        """ gray 스케일로 이미지 변환 => 2차원으로
        """

        grayImg = cv2.imread(imgPath, cv2.IMREAD_GRAYSCALE)
        start = time.time()
        img = cv2.filter2D(grayImg, -1, self.prewittKernelX)
        print(time.time() - start)
        # 0.0009951591491699219
        print (np.array(img))
        plt.figure()
        plt.imshow(img)
        plt.show()

def main():
    sobelObj = Prewitt()
    sobelObj.prewittOutLine()

if __name__ == "__main__":
    main()