from keras.models import load_model
from keras.preprocessing.image import img_to_array
import cv2
import numpy as np
import time


def start():
    # setting the classifiers
    face_classifier = cv2.CascadeClassifier(r'./Data/Emotion_Recognition/haarcascade_frontalface_default.xml')
    classifier = load_model(r'./Data/Emotion_Recognition/model.h5')
    emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']
    # opening the camera
    cap = cv2.VideoCapture(0)

    # camera timer
    timeout = 20
    timeout_start = time.time()

    results = list()
    print("started")
    while time.time() < timeout_start + timeout:
        _, frame = cap.read()
        labels = []
        # convert to gray
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # detect face
        faces = face_classifier.detectMultiScale(gray)

        for (x, y, w, h) in faces:
            # create the frame
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
            # Extract the ROI of the face from the grayscale image, resize it to a fixed size
            roi_gray = gray[y:y + h, x:x + w]
            roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)

            if np.sum([roi_gray]) != 0:
                # prepare the ROI for classification via the CNN
                roi = roi_gray.astype('float') / 255.0
                roi = img_to_array(roi)
                roi = np.expand_dims(roi, axis=0)
                # predict the emotion
                prediction = classifier.predict(roi)[0]
                label = emotion_labels[prediction.argmax()]
                label_position = (x, y)
                cv2.putText(frame, label, label_position, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                results.append(label)
                print(label)
            else:
                cv2.putText(frame, 'No Faces', (30, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow('Emotion Detector', frame)
        cv2.waitKey(1)

    cap.release()
    cv2.destroyAllWindows()

    return results
    # return max(results, key=results.count)
