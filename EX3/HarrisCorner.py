__author__ = "KimJunHyeon"
# ======================================
import cv2
import matplotlib.pyplot as plt
import numpy as np

class Harris:

    def __init__(self):
        self.imgObj = Harris.getCv2ImgObject()

    """ 해리스 코너 검출
    """
    def harrisConnerDetect(self):

        copyImg = self.imgObj.copy()

        # ===========================
        # img gray_scale 로 변환
        # ===========================
        grayImgObject  = cv2.cvtColor(self.imgObj, cv2.COLOR_BGR2GRAY)

        # ===========================
        # sobel
        # ===========================
        sobelImgObject = cv2.Sobel(grayImgObject,
                                   cv2.CV_8U,
                                   0,
                                   1,
                                   ksize=3)

        # ===========================
        # gaussian blurring
        # ===========================

        # ===========================
        # conner detection
        # ===========================
        dstImg = cv2.cornerHarris(self.doGausianBlurring(sobelImgObject), 2, 3, 0.01)
        dstImg = cv2.dilate(dstImg, None)
        copyImg[dstImg > 0.01 * dstImg.max()] = [0, 0, 255]
        plt.imshow(copyImg)
        plt.show()

    def doGausianBlurring(self, sobelImgObject):
        k = 17
        kernel = np.ones((k, k), np.float32) / (k ** 2)
        """
        ones => 
          1 1 1
          1 1 1
          1 1 1
        """
        filtering = cv2.filter2D(sobelImgObject, -1, kernel)
        return filtering



    """ cv2_img_object return 
    """
    @classmethod
    def getCv2ImgObject(cls):
        imgpath = r"C:\Users\junhyeon.kim\Desktop\AI_STU\imgCollecter\ferrari.jpg"
        return cv2.imread(imgpath)


def main():
    hObject = Harris()
    hObject.harrisConnerDetect()

if __name__ == "__main__":
    main()