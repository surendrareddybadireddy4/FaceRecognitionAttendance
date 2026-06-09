import cv2
import os
import numpy as np

path = "dataset/Surendra"

faces = []
ids = []

for file in os.listdir(path):

    if file.endswith(".jpg"):

        image_path = os.path.join(path, file)

        img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

        if img is not None:
            faces.append(img)
            ids.append(1)

print("Images loaded:", len(faces))

if len(faces) == 0:
    print("No valid images found!")
    exit()

recognizer = cv2.face.LBPHFaceRecognizer_create()

recognizer.train(faces, np.array(ids))

recognizer.save("trainer.yml")

print("Model trained successfully!")