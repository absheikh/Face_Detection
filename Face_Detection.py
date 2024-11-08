import cv2 # type: ignore
from random import randrange

# Loading some pre-trained data on face frontals from opencv
trained_face_data = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')

#Choosing an image to detect faces in
# img = cv2.imread(r"C:\Users\USER\Documents\Pyhton Proj\Face_Detection\faces.jpg")
# Capturing the video from the webcam
webcam = cv2.VideoCapture(0)

#Iterating forever over frames
while True:
    #Read the current frame
    successful_frame_read, frame = webcam.read()

    #Must convert to grayscale
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Detect faces
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

    #Draw rectangles around the faces
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (randrange(128,256), randrange(256), randrange(255)), 2)

    cv2.imshow("Face Detector", frame)
    key = cv2.waitKey(1)

    #Stop if Q key is pressed
    if key==81 or key==113:
        break

#Release the VideoCapture object
webcam.release()

