import cv2
import dlib
from deepface import DeepFace

detector = dlib.get_frontal_face_detector()
cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    for face in faces:
        x, y, w, h = face.left(), face.top(), face.width(), face.height()
        face_img = frame[y:y + h, x:x + w]

        try:
            # Analyser le visage
            analysis = DeepFace.analyze(face_img, actions=['age', 'emotion'], enforce_detection=False)

            # Si plusieurs visages sont détectés, analysis sera une liste
            if isinstance(analysis, list):
                analysis = analysis[0]  # Traiter seulement le premier visage détecté

            # Extraire l'âge et l'émotion dominante
            age = analysis.get('age', "Inconnu")
            emotion = analysis.get('dominant_emotion', "Inconnu")

            # Dessiner un rectangle autour du visage
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Afficher l'âge et l'émotion sur l'image
            cv2.putText(frame, f'Age: {age}', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)
            cv2.putText(frame, f'Emotion: {emotion}', (x, y + h + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)

        except Exception as e:
            print(f"Erreur: {e}")

    # Afficher l'image avec les annotations
    cv2.imshow('Age and Emotion Recognition', frame)

    # Quitter avec la touche 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libérer la caméra et fermer les fenêtres
cap.release()
cv2.destroyAllWindows()
