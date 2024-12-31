import cv2

# Test IP camera or local webcam
url = "http://192.168.1.39:8080/video"  # Replace with 0 for local webcam
video_stream = cv2.VideoCapture(1)

if not video_stream.isOpened():
    print("Error: Unable to access the video stream. Check the URL or webcam connection.")
else:
    while True:
        ret, frame = video_stream.read()
        if not ret:
            print("Error: Unable to read from the video stream.")
            break

        cv2.imshow("Webcam Test", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit
            break

    video_stream.release()
    cv2.destroyAllWindows()
