import cv2
import numpy as np
import matplotlib.pyplot as plt

class LaplacianMat:

    def __init__(self):

        self.laplacianKernel1 = np.array([
            [ 0, -1,  0],
            [-1,  4, -1],
            [ 0, -1,  0]
        ])

        self.laplacianKernel2 = np.array([
            [0,  1, 0],
            [1, -4, 1],
            [0,  1, 0]
        ])

        self.laplacianKernel3 = np.array([
            [-1, -1, -1],
            [-1, 8, -1],
            [-1, -1, -1]
        ])

        self.laplacianOfGaussianKernel = np.array([
            [+0, +0, -1, +0, +0],
            [+0, -1, -2, -1, +0],
            [-1, -2, 16, -2, -1],
            [+0, -1, -2, -1, +0],
            [+0, +0, -1, +0, +0],
        ])

    def laplacianOutline(self):


        imgPath = r"C:\Users\junhyeon.kim\Desktop\AI_STU\imgCollecter\ferrari.jpg"
        """ gray 스케일로 이미지 변환 => 2차원으로
        """
        grayImg = cv2.imread(imgPath, cv2.IMREAD_GRAYSCALE)
        kernel = np.ones((5, 5), np.float32) / (5 ** 2)
        img = cv2.filter2D(grayImg, -1, kernel)
        img = cv2.filter2D(img, -1, self.laplacianOfGaussianKernel)
        print (np.array(img))
        plt.figure()
        plt.imshow(img)
        plt.show()

def main():
    sobelObj = LaplacianMat()
    sobelObj.laplacianOutline()

if __name__ == "__main__":
    main()