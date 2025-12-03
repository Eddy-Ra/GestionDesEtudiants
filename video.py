import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
while True:
    re, frame = cap.read()
    cv2.imshow('Video Recording', frame)
    key = cv2.waitKey(0)

    if re:
        print("Recording started...")
        out.write(frame)
        if key == ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()







