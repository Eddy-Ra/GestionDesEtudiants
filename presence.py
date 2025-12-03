import datetime
import os
import sqlite3
from tkinter import messagebox
import cv2
import face_recognition
from les_func import parler, presence, voir_annonce


cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

imgbg = cv2.imread('too/IAE.png')
dossier_inconnu = "D:/bd/inconnu/"

folderPath = 'D:/bd/'
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
        files_in_inconnu = os.listdir(dossier_inconnu)

        if name == "Inconnu":
            imgbg[172:172 + 480, 78:78 + 640] = img
        else:

            new_photo_path = os.path.join(dossier, f'{name}.jpg')
            new_photo = cv2.imread(new_photo_path)
            new_photo_resized = cv2.resize(new_photo, (200, 200))
            img_height, img_width, _ = imgbg.shape
            imgbg[185:185 + 200, 960:960 + 200] = new_photo_resized
            key = cv2.waitKey(1) & 0xFF
            if key == ord('p'):
                date = datetime.datetime.now()
                parler(date)
                bd = sqlite3.connect("ma_base_de_donnees.db")
                con = bd.cursor()
                con.execute(f'SELECT * FROM listes')
                raw = con.fetchall()
                for row in raw:
                    id, n, p, s, c, a, da, tel, p1, anne = row
                    print(p)
                    if p == name:
                        presence(name, c, anne)
                        voir_annonce()
                        test = face_recognition.face_encodings(img)
                        if test:
                            encode = test[0]
                            known_faces.append(encode)
                            known_names.append(name)
                    else:
                        print("Vous devez faire un inscription")
                test = face_recognition.face_encodings(img)
                if test:
                    encode = test[0]
                    known_faces.append(encode)
                    known_names.append(name)
                print(name)
                messagebox.showinfo("Ok", "vous êtes présents")
        cv2.putText(img, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

    imgbg[172:172 + 480, 78:78 + 640] = img

    cv2.imshow("Presence", imgbg)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
