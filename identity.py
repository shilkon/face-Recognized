import string
import cv2
import os
import numpy as np
from data_return import *
from PIL import Image


def face_download(path_data: string, dict_face: dict):
    cam = cv2.VideoCapture(0)
    cam.set(3, 1280)  # set video width
    cam.set(4, 720)  # set video height

    face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # For each person, enter one numeric face id
    face_id = input('\n enter user id end press <return> ==>  ')

    print("\n [INFO] Initializing face capture. Look the camera and wait ...")
    # Initialize individual sampling face count
    count = 0

    if not os.path.exists(path_data):
        os.makedirs(path_data)

    while True:
        ret, img = cam.read()
        img = cv2.flip(img, 1)  # flip video image vertically
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.1, 3)

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            count += 1

            # Save the captured image into the datasets folder
            cv2.imwrite(path_data + "/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y + h, x:x + w])

        k = cv2.waitKey(100) & 0xff  # Press 'ESC' for exiting video
        if k == 27:
            break
        elif count >= 100:  # Take 60 face sample and stop video
            break

    # Do a bit of cleanup
    print("\n [INFO] Exiting Program and cleanup stuff")
    cam.release()
    cv2.destroyAllWindows()


def face_training(path_date, path_trainer):
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml");

    print("\n [INFO] Training faces. It will take a few seconds. Wait ...")
    faces, ids = getImagesAndLabels(path_date, detector)
    recognizer.train(faces, np.array(ids))

    if not os.path.exists(path_trainer):
        os.makedirs(path_trainer)

    # Save the model into trainer/trainer.yml
    recognizer.write(path_trainer + "/trainer.yml")  # recognizer.save() worked on Mac, but not on Pi

    # Print the numer of faces trained and end program
    print("\n [INFO] {0} faces trained. Exiting Program".format(len(np.unique(ids))))


def face_recognation(path_trainer, dict_face: dict, faceCascade) -> InfoRecognize:
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read(path_trainer + "/trainer.yml")

    # Initialize and start realtime video capture
    cam = cv2.VideoCapture(0)
    cam.set(3, 1280)  # set video widht
    cam.set(4, 720)  # set video height

    # Define min window size to be recognized as a face
    minW = 0.1 * cam.get(3)
    minH = 0.1 * cam.get(4)

    i = 0
    while True:
        ret, img = cam.read()
        img = cv2.flip(img, 1)  # Flip vertically

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=3,
            minSize=(int(minW), int(minH)),
        )

        for (x, y, w, h) in faces:

            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

            id, confidence = recognizer.predict(gray[y:y + h, x:x + w])

            # Check if confidence is less them 100 ==> "0" is perfect match
            if (confidence < 100):
                if 100 - confidence > 60:
                    print("\n [INFO] Recognized person")
                    cam.release()
                    return InfoRecognize(Condition.RECOGNIZED, dict_face[id])

            #print(confidence, '\n')
            
            i += 1
            if (i >= 10):
                print("\n [INFO] Unknown person")
                cam.release()
                return InfoRecognize(Condition.UNKNOWN, 'None')



# function to get the images and label data
def getImagesAndLabels(path_date, detector):
    imagePaths = [os.path.join(path_date, f) for f in os.listdir(path_date)]
    faceSamples = []
    ids = []

    for imagePath in imagePaths:

        PIL_img = Image.open(imagePath).convert('L')  # convert it to grayscale
        img_numpy = np.array(PIL_img, 'uint8')

        id = int(os.path.split(imagePath)[-1].split(".")[1])
        faces = detector.detectMultiScale(img_numpy)

        for (x, y, w, h) in faces:
            faceSamples.append(img_numpy[y:y + h, x:x + w])
            ids.append(id)

    return faceSamples, ids
