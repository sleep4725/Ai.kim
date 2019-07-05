import cv2
import yaml
import numpy as np
import matplotlib.pyplot as plt

class Gausian:

    def __init__(self):
        self.imgObj = Gausian.getImgPath()

    def doGausianBlurring(self, imgObj):
        for k in range(5, 21, 5):
            kernel = np.ones((k, k), np.float32)/(k**2)
            print (kernel)
            """
            ones => 
              1 1 1
              1 1 1
              1 1 1
            """
            filtering = cv2.filter2D(imgObj, -1, kernel)
            plt.subplot(1, 4, k/5) # 1행 3열
            plt.imshow(filtering)
            plt.title("kernel size {s}".format(s = k))
            plt.axis("off")
        plt.show()

    def testImgCal(self):
        kernel = np.array(
            [
                [0,  0,  0],
                [0, -1,  0],
                [0,  1,  0]
            ]
        )

        calculusImg = cv2.filter2D(self.imgObj, -1, kernel)
        #self.doGausianBlurring(calculusImg)
        plt.figure()
        plt.imshow(calculusImg)
        plt.show()

    @classmethod
    def getImgPath(cls):
        tmpPath = r"C:\Users\junhyeon.kim\Desktop\AI_STU\Stu01\confg\info.yaml"
        with open(tmpPath, "r", encoding="utf") as f:
            tmpImgObj = dict(yaml.load(f, yaml.Loader))["imgpath"]
            f.close()
        return cv2.imread(tmpImgObj, cv2.IMREAD_GRAYSCALE)

def main():
    gnode = Gausian()# 객체 생성
    #gnode.doGausianBlurring()
    gnode.testImgCal()

if __name__ == "__main__":
    main()