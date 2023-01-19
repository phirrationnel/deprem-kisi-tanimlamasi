import face_recognition
import cv2
import numpy as np

video_capture = cv2.VideoCapture(0)


umut = face_recognition.load_image_file("umut.jpg")
umut_yüz = face_recognition.face_encodings(umut)[0]

ali = face_recognition.load_image_file("ali2.jpg")
ali_yüz = face_recognition.face_encodings(ali)[0]

#ufuk = face_recognition.load_image_file("ufuk.jpg")
#ufuk_yüz = face_recognition.load_image_file(ufuk)[0]

mthami = face_recognition.load_image_file("mthami.jpg")
mthami_yüz = face_recognition.face_encodings(mthami)[0]


işlenebilirler = [
    umut_yüz,
    ali_yüz,
    mthami_yüz,
    #ufuk_yüz,
]
bilinenler = [
    "Umut",
    "Ali",
    "M.Thami",
    "Ufuk"
]

face_locations = []
face_encodings = []
face_names = []
detected = []
process_this_frame = True

while True:

    ret, frame = video_capture.read()

    if process_this_frame:

        dikdörtgen = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        renkli_dikdörtgen = dikdörtgen[:, :, ::-1]



        face_locations = face_recognition.face_locations(renkli_dikdörtgen)
        face_encodings = face_recognition.face_encodings(renkli_dikdörtgen, face_locations)


        face_names = []
        for face_encoding in face_encodings:

            matches = face_recognition.compare_faces(işlenebilirler, face_encoding)
            name = "Bilinmeyen"


            face_distances = face_recognition.face_distance(işlenebilirler, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = bilinenler[best_match_index]
                detected.append(name)
                my_set = set(detected)

            face_names.append(name)



    process_this_frame = not process_this_frame


    for (top, right, bottom, left), name in zip(face_locations, face_names):

        top *= 4
        right *= 4
        bottom *= 4
        left *= 4


        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)


        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)


    cv2.imshow('Kamera 1', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



with open('okuldaolanlar.txt', 'w') as fp:
    for item in my_set:
        fp.write("%s\n" % item)

video_capture.release()
cv2.destroyAllWindows()
