import cv2
import os

# Folder to save images
folder = "dataset/Surendra"

if not os.path.exists(folder):
    os.makedirs(folder)

# Face detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

cap = cv2.VideoCapture(0)

count = 0

while True:
    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:

        face = frame[y:y+h, x:x+w]

        count += 1

        filename = os.path.join(folder, f"face_{count}.jpg")

        cv2.imwrite(filename, face)

        print(f"Saved: {filename}")

        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow("Capture Faces", frame)

    if count >= 30:
        print("30 images saved!")
        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()