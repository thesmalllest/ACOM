import cv2
import numpy as np

# task 1 2 3
def non_max_suppression(magnitude, angle):
    H, W = magnitude.shape
    suppressed = np.zeros((H, W), dtype=np.float32)

    angle = np.rad2deg(angle) % 180

    for y in range(1, H - 1):
        for x in range(1, W - 1):
            q = 255
            r = 255

            # grad direction
            ang = angle[y, x]

            # 0 deg (right-left)
            if (0 <= ang < 22.5) or (157.5 <= ang <= 180):
                q = magnitude[y, x + 1]
                r = magnitude[y, x - 1]

            # 45 grad 
            elif 22.5 <= ang < 67.5:
                q = magnitude[y + 1, x - 1]
                r = magnitude[y - 1, x + 1]

            # 90 deg (up-down)
            elif 67.5 <= ang < 112.5:
                q = magnitude[y + 1, x]
                r = magnitude[y - 1, x]

            # 135 grad 
            elif 112.5 <= ang < 157.5:
                q = magnitude[y - 1, x - 1]
                r = magnitude[y + 1, x + 1]

            # saving only loc max
            if magnitude[y, x] >= q and magnitude[y, x] >= r:
                suppressed[y, x] = magnitude[y, x]

    return suppressed

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

    # supression
    suppressed = non_max_suppression(magnitude, angle)

    mag_norm = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
    sup_norm = cv2.normalize(suppressed, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

    cv2.imshow("B&W", gray)
    cv2.imshow("Grad magnitute", mag_norm)
    cv2.imshow("After Non-Max Suppression", sup_norm)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    process_image("balerion.jpg")
