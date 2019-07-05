from PIL import Image
from PIL import ImageFilter
import matplotlib.pyplot as plt

__author__ = "KimJunHyeon"

class GaussianBlur:

    def __init__(self):
        self.imgObj = GaussianBlur.getImgPath()

    def doBluring(self):
        r, c = 1, 1
        flag = 0
        for sigma in range(1, 6, 1):
            Gaussian_Blur = self.imgObj.filter(ImageFilter.GaussianBlur(sigma))
            plt.subplot(1, 6, sigma)  # 1행 3열

            """
            c = c + 1
            flag = c//3
            if flag == 1:
                r = r + flag
                c = 1
            """

            plt.imshow(Gaussian_Blur)
            plt.title("sigma size {s}".format(s=sigma))
            plt.axis("off")
        plt.show()

    @classmethod
    def getImgPath(cls):
        return Image.open("C:\\Users\\junhyeon.kim\\Desktop\\AI_STU\\imgCollecter\\ferrari.jpg")

def main():
    imgGaussian = GaussianBlur()
    imgGaussian.doBluring()

if __name__ == "__main__":
    main()


