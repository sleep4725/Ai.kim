from PIL import Image

imgPaths = r"C:\Users\junhyeon.kim\Desktop\PILtutorial\AI\Ex01\test_imgs\dog.jpeg"
dogImgs  = Image.open(imgPaths)

# 이미지 보기
dogImgs.show()