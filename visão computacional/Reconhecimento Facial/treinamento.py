import PIL 
import PIL.Image
import cv2
import os
import numpy as np
import face_recognition


facesTrain = []
nameTrain = []
folder = "Jairzinho"
paths = [os.path.join(f"family/{folder}", f) for f in os.listdir(f"family/{folder}")]
for path in paths:
    image = face_recognition.load_image_file(path)
    encoding = face_recognition.face_encodings(image)[0]
    print(path)
    facesTrain.append(encoding)
    nameTrain.append(folder)

folder = "Test"
paths = [os.path.join(f"family/{folder}", f) for f in os.listdir(f"family/{folder}")]
for path in paths:
    image = face_recognition.load_image_file(path)
    locations = face_recognition.face_locations(image)
    encodings = face_recognition.face_encodings(image, locations)
    print(path)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    for face_encoding, face_location in zip(encodings, locations):
        results = face_recognition.compare_faces(facesTrain, face_encoding, 0.6)
        face_distances = face_recognition.face_distance(facesTrain, face_encoding)
        best_match_index = np.argmin(face_distances)
        print(best_match_index)
        if results[best_match_index]:
            name = nameTrain[best_match_index]
            topLeft = (face_location[3], face_location[0])
            bottomRight = (face_location[1], face_location[2])
            color = [0, 255, 0]
            cv2.rectangle(image, topLeft, bottomRight, color, 3)

            topLeft = (face_location[3], face_location[2])
            bottomRight = (face_location[1], face_location[2]+22)
            cv2.rectangle(image, topLeft, bottomRight, color, cv2.FILLED)
            cv2.putText(image, name, (face_location[3]+10, face_location[2]+15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), 3)
    cv2.namedWindow("output", cv2.WINDOW_NORMAL)
    cv2.imshow("output", image)
    cv2.resizeWindow("output", 600, 600)
    cv2.waitKey(0)
   