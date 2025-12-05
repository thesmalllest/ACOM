import cv2
import numpy as np

# task 1 2 3 4
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

def double_threshold(img, low_ratio=0.05, high_ratio=0.15):
    high = img.max() * high_ratio
    low = high * low_ratio

    H, W = img.shape
    res = np.zeros((H, W), dtype=np.uint8)

    strong = 255
    weak = 80

    strong_y, strong_x = np.where(img >= high)
    weak_y, weak_x = np.where((img <= high) & (img >= low))

    res[strong_y, strong_x] = strong
    res[weak_y, weak_x] = weak

    return res, weak, strong

def hysteresis(img, weak=80, strong=255):
    H, W = img.shape

    for y in range(1, H - 1):
        for x in range(1, W - 1):
            if img[y, x] == weak:
                # Если хотя бы один сосед сильный — делаем пиксель сильным
                if (img[y+1, x-1] == strong or img[y+1, x] == strong or img[y+1, x+1] == strong or
                    img[y,   x-1] == strong or img[y,   x+1] == strong or
                    img[y-1, x-1] == strong or img[y-1, x] == strong or img[y-1, x+1] == strong):
                    img[y, x] = strong
                else:
                    img[y, x] = 0  

    return img

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

    # double threshold
    dt, weak, strong = double_threshold(suppressed)

    # hysteresis
    final_edges = hysteresis(dt, weak, strong)

    mag_norm = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
    sup_norm = cv2.normalize(suppressed, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

    cv2.imshow("B&W", gray)
    cv2.imshow("Grad magnitute", mag_norm)
    cv2.imshow("After Non-Max Suppression", sup_norm)
    cv2.imshow("Double Threshold", dt)
    cv2.imshow("Edges After Hysteresis", final_edges)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    process_image("balerion.jpg")
