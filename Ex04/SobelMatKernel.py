import cv2
import numpy as np
import matplotlib.pyplot as plt
import time

class SobelMat:

    def __init__(self):
        ## x축 sobel
        self.sobelKernelX = np.array([
            [-1, 0, +1],
            [-2, 0, +2],
            [-1, 0, +1]
        ])

        ## y축 sobel
        self.sobelKernelY = np.array([
            [+1, +2, +1],
            [ 0,  0,  0],
            [-1, -2, -1]
        ])
    def sobelOutline(self):


        imgPath = r"C:\Users\junhyeon.kim\Desktop\AI_STU\imgCollecter\ferrari.jpg"
        """ gray 스케일로 이미지 변환 => 2차원으로
        """

        grayImg = cv2.imread(imgPath, cv2.IMREAD_GRAYSCALE)
        start = time.time()

        # ============================================================
        # blurring
        # ============================================================
        kernel = np.ones((5, 5), np.float32) / (5 ** 2)
        img = cv2.filter2D(grayImg, -1, kernel)
        img = cv2.filter2D(img, -1, self.sobelKernelY)
        print (time.time() - start)
        # 0.001995086669921875
        print (np.array(img))
        plt.figure()
        plt.imshow(img)
        plt.show()

def main():
    sobelObj = SobelMat()
    sobelObj.sobelOutline()

if __name__ == "__main__":
    main()