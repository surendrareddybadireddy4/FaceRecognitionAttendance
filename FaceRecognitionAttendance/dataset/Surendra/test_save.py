import cv2

cap = cv2.VideoCapture(0)

ret, frame = cap.read()

if ret:
    cv2.imwrite("test.jpg", frame)
    print("Image saved successfully!")
else:
    print("Failed to capture image")

cap.release()