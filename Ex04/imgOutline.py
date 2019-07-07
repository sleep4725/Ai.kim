##
# 이미지 윤곽선 검출
##
# ============================================
from skimage import measure
from skimage.io import imread
from skimage.color import rgb2gray
from skimage.filters import sobel
import matplotlib.pyplot as plt
# ============================================

class ImgOutline:

    def __init__(self):
        self.imgObj = imread(ImgOutline.imgPathReturn())

    def imgStep(self):
        # ===============================
        # Gray scale로 변환
        # ===============================
        imgGray = rgb2gray(self.imgObj)

        # 이미지에서 edge 검출
        imgEdge = sobel(imgGray)

        # 이미지에서 윤곽 검출
        #contours = measure.find_contours(imgEdge, 0.2)

        # 이미지와 찾은 윤곽선 표시
        """
        fig, ax = plt.subplots()

        ax.imshow(imgEdge, interpolation="nearest", cmap=plt.cm.gray)
        for n, contour in enumerate(contours):
            ax.plot(contour[:,1], contour[:,0], linewidth=2)

        ax.axis("mage")
        ax.set_xticks([])
        ax.set_yticks([])
        plt.show()
        """
    @classmethod
    def imgPathReturn(cls):

        path = r"C:\Users\junhyeon.kim\Desktop\PILtutorial\Ai.kim\Ex04\test_img"
        return path

def main():
    obj = ImgOutline()
    obj.imgStep()

if __name__ == "__main__":
    main()