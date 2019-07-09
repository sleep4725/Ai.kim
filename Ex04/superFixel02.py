from skimage.segmentation import slic, watershed
from skimage.segmentation import mark_boundaries
from skimage.util import img_as_float
import cv2

# load the image and apply SLIC
image = cv2.imread(r"C:\Users\junhyeon.kim\Desktop\AI_STU\imgCollecter\ferrari.jpg")
## Change the n_segments and sigma values to fit your needs
segments = slic(img_as_float(image), n_segments = 200, sigma = 4)

bounds = mark_boundaries(image, segments)

cv2.imshow("bounds", bounds)
cv2.waitKey(0)
cv2.destroyAllWindows()