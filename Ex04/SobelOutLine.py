import cv2

class SobelOUTline:

    def __init__(self):
        # ========================
        # 이미지 불러오기
        # ========================
        self.imgObj = cv2.imread(SobelOUTline.imgGet())

    def sobelLine(self):
        # ========================
        # 원본 이미지 gray로 변환
        # ========================
        grayImg  = cv2.cvtColor(self.imgObj, cv2.COLOR_BGR2GRAY)

        # ========================
        # x축
        # ========================
        sobelObj = cv2.Sobel(grayImg, -1, 1, 0, ksize=5)

        # ========================
        # y축
        # ========================
        sobelObj = cv2.Sobel(grayImg, -1, 0, 1, ksize=5)
        cv2.imshow("x edge_image", sobelObj)
        cv2.waitKey()

    def test01(self):
        grayImg = cv2.cvtColor(self.imgObj, cv2.COLOR_BGR2GRAY)
        lapla = cv2.Laplacian(grayImg, cv2.CV_64F)
        cv2.imshow("lapla", lapla)
        cv2.waitKey()

    @classmethod
    def imgGet(cls):

        imgPath = "C:\\Users\\junhyeon.kim\\Desktop\\PILtutorial\\Ai.kim\\Ex04\\test_img\\iron.jpg"
        return imgPath


def main ():
    obj = SobelOUTline()
    obj.test01()

if __name__ == "__main__":
    main()