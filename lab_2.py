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

if __name__ == "__main__":
    pic_from_cam_to_hsv()
