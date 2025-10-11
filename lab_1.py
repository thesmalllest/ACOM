# Task 1

import cv2

# Task 2 Работа с изображениями
def show_image():
    img_jpg = cv2.imread(r'zayki.jpg', cv2.IMREAD_COLOR) 
    img_png = cv2.imread(r'zayki.png', cv2.IMREAD_GRAYSCALE) 
    img_bmp = cv2.imread(r'zayki.bmp', cv2.IMREAD_UNCHANGED)
    
    cv2.namedWindow('Window Normal', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Window Normal', 370, 600)
    cv2.imshow('Window Normal', img_jpg)
    cv2.waitKey(0)

    cv2.namedWindow('Window Autosize', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('Window Autosize', img_png)
    cv2.waitKey(0)

    cv2.namedWindow('Window Fullscreen', cv2.WINDOW_FULLSCREEN)
    cv2.imshow('Window Fullscreen', img_bmp)
    cv2.waitKey(0)

    cv2.destroyAllWindows()

# Task 3 Работа с видео
def play_video():
    cap = cv2.VideoCapture(r'lashadka.mp4')

    cv2.namedWindow('Video', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Video', 370, 600)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:  
            break
        cv2.imshow('Video', frame)
        if cv2.waitKey(15) & 0xFF == 27:  
            break

    cap.release()
    cv2.destroyAllWindows()

# Task 4 Запись видео из файла в другой файлRecord video from file to another file
def copy_video_to_file():
    cap = cv2.VideoCapture(r'lashadka.mp4')  

    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps    = cap.get(cv2.CAP_PROP_FPS)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    # cv2.VideoWriter(filename, fourcc, fps, size)
    out = cv2.VideoWriter('copy_output.mp4', fourcc, fps, (width, height))

    cv2.namedWindow('Copying Video', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Copying Video', 370, 600)

    while True:
        ret, frame = cap.read()
        if not ret:  
            break

        out.write(frame)               
        cv2.imshow('Copying Video', frame)

        if cv2.waitKey(1) & 0xFF == 27:  
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

# Task 5 Перевод изображения в HSV
def show_color_and_hsv():
    frame = cv2.imread(r'zayki.jpg', cv2.IMREAD_COLOR)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  

    cv2.namedWindow('Color Image', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Color Image', 370, 600)
    cv2.imshow('Color Image', frame)

    cv2.namedWindow('HSV Image', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('HSV Image', 370, 600)
    cv2.imshow('HSV Image', hsv)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Task 6 Крест в центре кадра
def draw_cross_from_cam():
    cap = cv2.VideoCapture(0)        
    cap.set(3, 640)   # 3 - width               
    cap.set(4, 480)   # 4 - height  

    while True:
        ret, frame = cap.read()    
        if not ret:
            break

        h, w = frame.shape[:2]
        center_x, center_y = w // 2, h // 2

        # cv2.line(image, start_point, end_point, color(B,G,R), thickness)
        cv2.line(frame, (center_x - 50, center_y), (center_x + 50, center_y), (0, 0, 255), 3)
        cv2.line(frame, (center_x, center_y - 50), (center_x, center_y + 50), (0, 0, 255), 3)

        cv2.imshow('Camera with Cross', frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

# Task 7 Отображение и запись видео с веб-камеры
def record_and_play_cam():
    cap = cv2.VideoCapture(0)      
    cap.set(3, 640)                  
    cap.set(4, 480)                 

    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps    = 25.0

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    filename = 'webcam_record.mp4'
    out = cv2.VideoWriter(filename, fourcc, fps, (width, height))

    cv2.namedWindow('Webcam Recording', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Webcam Recording', 370, 600)

    # Чтение и запись с камеры 
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        out.write(frame)                      
        cv2.imshow('Webcam Recording', frame) 

        if cv2.waitKey(1) & 0xFF == 27:       
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

    play = cv2.VideoCapture(filename)

    cv2.namedWindow('Playback', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Playback', 370, 600)

    while True:
        ret, frame = play.read()
        if not ret:
            break
        cv2.imshow('Playback', frame)

        if cv2.waitKey(30) & 0xFF == 27:       
            break

    play.release()
    cv2.destroyAllWindows()

# Task 8 Определение цвета центра кадра
def task8():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  
    cap.set(3, 640)
    cap.set(4, 480)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)

        h, w = frame.shape[:2]
        x, y = w // 2, h // 2  # центр кадра
        b, g, r = frame[y, x] # цвет цкнтрального пикселя

        if r >= g and r >= b:
            color = (0, 0, 255)   # красный
        elif g >= r and g >= b:
            color = (0, 255, 0)   # зелёный
        else:
            color = (255, 0, 0)   # синий

        cv2.rectangle(frame, (x - 100, y - 15), (x + 100, y + 15), color, -1)
        cv2.rectangle(frame, (x - 15, y - 100), (x + 15, y + 100), color, -1)

        cv2.imshow('Color Cross', frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

# Task 9 Подключение телефона через Camo Camera
def camo_camera():
    cap = cv2.VideoCapture(1)  

    cv2.namedWindow('Camo Camera', cv2.WINDOW_AUTOSIZE)
   
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow('Camo Camera', frame)
        if cv2.waitKey(1) & 0xFF == 27:  
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # show_image()       
    # play_video()     
    # copy_video_to_file()   
    # show_color_and_hsv()  
    # draw_cross_from_cam()
    # record_and_play_cam()
    # task8()
    camo_camera()

