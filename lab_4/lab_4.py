import cv2
import numpy as np

# task 1 2
def process_image(path):
    img = cv2.imread(path)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (7, 7), 0)

    # Sobel grad
    grad_x = cv2.Sobel(blurred, cv2.CV_64F, 1, 0, ksize=3)  # Derivative X
    grad_y = cv2.Sobel(blurred, cv2.CV_64F, 0, 1, ksize=3)  # Derivative Y

    # grad height
    magnitude = np.sqrt(grad_x**2 + grad_y**2)

    # grad angle
    angle = np.arctan2(grad_y, grad_x)

    print("Grad matrix:\n", magnitude)
    print("\nGrad angle matrix:\n", angle)

    mag_norm = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
    ang_norm = cv2.normalize(angle, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

    cv2.imshow("B&W", gray)
    cv2.imshow("Grad magnitute", mag_norm)
    cv2.imshow("Grad angle", ang_norm)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    process_image("balerion.jpg")
