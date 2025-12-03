import cv2
import mediapipe as mp

# Initialiser Mediapipe pour la détection de la main
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Initialiser la webcam
cap = cv2.VideoCapture(1)

with mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Convertir l'image en RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False

        # Détection des mains
        results = hands.process(image)

        # Revenir à BGR pour l'affichage
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Dessiner les landmarks de la main
                mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Obtenir les positions des landmarks (points clés)
                landmarks = hand_landmarks.landmark

                # Positions des bouts des doigts
                fingertips = [landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP],
                              landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_TIP],
                              landmarks[mp_hands.HandLandmark.RING_FINGER_TIP]]

                # Dessiner des points au bout des doigts
                h, w, _ = image.shape
                for fingertip in fingertips:
                    x, y = int(fingertip.x * w), int(fingertip.y * h)
                    cv2.circle(image, (x, y), 10, (0, 255, 0), -1)  # Cercle vert

                # Vérifier si les trois doigts sont levés
                fingers_up = [
                    landmarks[mp_hands.HandLandmark.THUMB_TIP].y < landmarks[mp_hands.HandLandmark.THUMB_IP].y,
                    landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP].y < landmarks[
                        mp_hands.HandLandmark.INDEX_FINGER_DIP].y,
                    landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y < landmarks[
                        mp_hands.HandLandmark.MIDDLE_FINGER_DIP].y,
                    landmarks[mp_hands.HandLandmark.RING_FINGER_TIP].y < landmarks[
                        mp_hands.HandLandmark.RING_FINGER_DIP].y,
                    landmarks[mp_hands.HandLandmark.PINKY_TIP].y < landmarks[mp_hands.HandLandmark.PINKY_DIP].y]

                # On compte les doigts levés (1 si levé, 0 sinon)
                if fingers_up == [False, True, True, True, False]:
                    cv2.putText(image, 'Three Fingers Up!', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2,
                                cv2.LINE_AA)

        # Afficher l'image
        cv2.imshow('Hand Gesture', image)

        # Quitter avec la touche 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Libérer la caméra et fermer les fenêtres
cap.release()
cv2.destroyAllWindows()
