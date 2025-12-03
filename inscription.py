import os
import cv2
import face_recognition
import dlib
from BD import enregister, etudiantsbd
from func_int import interface
from les_func import parler, apropos

cap = cv2.VideoCapture(0)

cap.set(5, 640)
cap.set(5, 640)

imgbg = cv2.imread('too/IAE.png')
dossier = "D:/bd/"
dossier1 = "D:/bd/inconnu/"
imageListe = []
known_faces = []
known_names = []

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
        prenoms = "Inconnu"

        if True in matches:
            first_match_index = matches.index(True)
            prenoms = known_names[first_match_index]
        key = cv2.waitKey(1) & 0xFF
        if prenoms != "Inconnu":
            print("Vous êtes déjà inscrit")
            parler(f"Monsieur {prenoms} Vous êtes déjà inscrit")
            test = face_recognition.face_encodings(img)
            apropos(prenoms, "See timetable")
            if test:
                encode = test[0]
                known_faces.append(encode)
                known_names.append(prenoms)
            print(prenoms)

        else:
            cv2.imwrite(os.path.join(dossier1, f"{prenoms}.jpg"), img)
        if key == ord('e'):
            if prenoms == "Inconnu":
                cv2.imwrite(os.path.join(dossier1, f"{prenoms}.jpg"), img)
                name, prenoms, classe, date, age, tel, genre, anne = interface(prenoms)
                presence = 0
                cv2.imwrite(os.path.join(dossier, f"{prenoms}.jpg"), img)
                enregister(name, prenoms, genre, classe, age, date, tel, os.path.join(dossier, f"{prenoms}.jpg"), anne)
                etudiantsbd(name, prenoms, genre, classe, age, date, tel, os.path.join(dossier, f"{prenoms}.jpg"),
                            presence, anne)
                test = face_recognition.face_encodings(img)
                if test:
                    encode = test[0]
                    known_faces.append(encode)
                    known_names.append(prenoms)
                print(f"Photo de {prenoms} enregistrée avec succès!")
                parler(f"Photo de {prenoms} enregistrée avec succès!")
                apropos(prenoms, "See timetable")

        cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 2)
        font = cv2.FONT_HERSHEY_DUPLEX
        files_in_inconnu = os.listdir(dossier1)
        if prenoms != "Inconnu":
            new_photo_path = os.path.join(dossier, f'{prenoms}.jpg')
            new_photo = cv2.imread(new_photo_path)
            new_photo_resized = cv2.resize(new_photo, (200, 200))

            imgbg[185:185 + 200, 960:960 + 200] = new_photo_resized
        else:
            new_photo_path = os.path.join(dossier1, f'{prenoms}.jpg')
            new_photo = cv2.imread(new_photo_path)
            new_photo_resized = cv2.resize(new_photo, (200, 200))

            imgbg[185:185 + 200, 960:960 + 200] = new_photo_resized

        cv2.putText(img, prenoms, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)
        cv2.putText(imgbg, prenoms, (20, 50), font, 20, (255, 255, 20), 1)

    imgbg[172:172 + 480, 78:78 + 640] = img

    cv2.imshow("Inscription", imgbg)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
