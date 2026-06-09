import cv2
from datetime import datetime

# Load trained model
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml")

# Face detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

name = "Surendra"
attendance_marked = False

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to access webcam")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5
    )

    for (x, y, w, h) in faces:

        face = gray[y:y+h, x:x+w]

        id, confidence = recognizer.predict(face)

        if confidence < 100:

            cv2.putText(
                frame,
                name,
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 0),
                2
            )

            if not attendance_marked:

                now = datetime.now()

                date = now.strftime("%d-%m-%Y")
                time = now.strftime("%H:%M:%S")

                already_marked = False

                with open("attendance.csv", "r") as file:
                    records = file.readlines()

                for record in records:
                    if name in record and date in record:
                        already_marked = True
                        break

                if not already_marked:
                    with open("attendance.csv", "a") as file:
                        file.write(f"{name},{date},{time}\n")

                    print("Attendance Marked!")
                else:
                    print("Attendance Already Marked Today")

                attendance_marked = True

        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (255, 0, 0),
            2
        )

    cv2.imshow("Face Recognition Attendance", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()