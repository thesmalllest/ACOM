import cv2

# task 1
def pic_from_cam_to_hsv():
    cap = cv2.VideoCapture(1)
    if not cap.isOpened():
        print("Ошибка: не удалось открыть камеру")
        exit()

    ret, frame = cap.read()

    if not ret:
        print("Не удалось получить кадр")
        cap.release()
        exit()

    hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    cv2.imshow('BGR', frame)
    cv2.imshow('HSV', hsv_image)

    cv2.imwrite("original.jpg", frame)
    cv2.imwrite("hsv_image.jpg", hsv_image)

    cv2.waitKey(0)

    cap.release()
    cv2.destroyAllWindows()

# task 2
def filter_red_from_image():
 
    image = cv2.imread("cvetok.jpg")
    image = cv2.resize(image, (600, 400))

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Нижний диапазон красного (0–10)
    lower_red1 = (0, 120, 70)
    upper_red1 = (10, 255, 255)

    # Верхний диапазон красного (170–180)
    lower_red2 = (170, 120, 70)
    upper_red2 = (180, 255, 255)

    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

    red_mask = cv2.bitwise_or(mask1, mask2)

    red_filtered = cv2.bitwise_and(image, image, mask=red_mask)

    cv2.imshow('Original', image)
    cv2.imshow('Red Mask (Threshold)', red_mask)
    cv2.imshow('Filtered (Red only)', red_filtered)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # pic_from_cam_to_hsv()
    filter_red_from_image()
