# File: register_faces.py
import os
import pickle
import face_recognition
from config import DATA_DIR, KNOWN_FACES_PATH

def register_known_faces(images_dir):
    known_encodings = []
    known_names = []
    for img_file in os.listdir(images_dir):
        if img_file.lower().endswith((".jpg",".png")):
            img = face_recognition.load_image_file(os.path.join(images_dir, img_file))
            encs = face_recognition.face_encodings(img)
            if encs:
                known_encodings.append(encs[0])
                known_names.append(os.path.splitext(img_file)[0])
    with open(KNOWN_FACES_PATH,"wb") as f:
        pickle.dump((known_encodings, known_names), f)

if __name__=="__main__":
    os.makedirs(DATA_DIR, exist_ok=True)
    register_known_faces(os.path.join(DATA_DIR,"known_faces_images"))
  
