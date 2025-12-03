import os
import cv2
import face_recognition

# Essayez différents numéros de caméra (0, 1, 2, etc.) en fonction de votre configuration
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

imgbg = cv2.imread('../bg/IAE.png')

folderPath = '../ranto/too'
modePath = os.listdir(folderPath)
imageListe = []
for pic in modePath:
    imageListe.append(cv2.imread(os.path.join(folderPath, pic)))

known_faces = []
known_names = []
dossier = "D:/bd/"
for sary in os.listdir(dossier):
    if sary.endswith('.jpg'):
        place = face_recognition.load_image_file(os.path.join(dossier, sary))
        test = face_recognition.face_encodings(place)
        if test:
            encode = test[0]
            known_faces.append(encode)
            known_names.append(os.path.splitext(sary)[0])

while True:
    success, img = cap.read()

    face_locations = face_recognition.face_locations(img)
    face_encodings = face_recognition.face_encodings(img, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_faces, face_encoding, tolerance=0.5)
        name = "Inconnu"

        if True in matches:
            first_match_index = matches.index(True)
            name = known_names[first_match_index]

        cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 2)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(img, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

    imgbg[172:172 + 480, 78:78 + 640] = img
    imgbg[185:185 + 200, 960:960 + 200] = imageListe[1]

    cv2.imshow("FaceRecognition", imgbg)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
