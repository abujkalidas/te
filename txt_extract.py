import cv2

def list_cameras():
    index = 0
    while True:
        cap = cv2.VideoCapture(index)
        if not cap.isOpened():
            break
        print(f"Camera available at index {index}")
        cap.release()
        index += 1

list_cameras()
