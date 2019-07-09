import cv2
import numpy as np
import matplotlib.pyplot as plt

""" 프리윗
"""
class RobertsKernel:

    def __init__(self):
        ## x축 prewitt
        self.robertsKernelX = np.array([
            [-1, +0, +0],
            [+0, +1, +0],
            [+0, +0, +0]
        ])

    def robertsOutLine(self):

        imgPath = r"C:\Users\junhyeon.kim\Desktop\AI_STU\imgCollecter\ferrari.jpg"

        """ gray 스케일로 이미지 변환 => 2차원으로
        """
        grayImg = cv2.imread(imgPath, cv2.IMREAD_GRAYSCALE)

        img = cv2.filter2D(grayImg, -1, self.robertsKernelX)
        print (np.array(img))
        plt.figure()
        plt.imshow(img)
        plt.show()

def main():
    sobelObj = RobertsKernel()
    sobelObj.robertsOutLine()

if __name__ == "__main__":
    main()