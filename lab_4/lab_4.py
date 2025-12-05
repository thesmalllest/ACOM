import cv2

# task 1
def process_image(path):
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imshow("B&W", gray)
    
    blurred = cv2.GaussianBlur(gray, (7, 7), 0)
    cv2.imshow("Blur", blurred)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    process_image("cvetok.jpg")