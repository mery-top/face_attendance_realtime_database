import cv2
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':'https://faceattendance-f663d-default-rtdb.firebaseio.com/',
    'storageBucket' : 'faceattendance-f663d.appspot.com'
})

#importing mode images into a list

folderPath = 'images'
PathList = os.listdir(folderPath)
print(PathList)
imglist = []
studentids= []
for path in PathList:
    imglist.append(cv2.imread(os.path.join(folderPath, path)))
    studentids.append(os.path.splitext(path)[0])

    filename = f'{folderPath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(filename)
    blob.upload_from_filename(filename)


print(studentids)

def readencodings(imagelist):
    encodelist = []
    for img in imagelist:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodelist.append(encode)
    return encodelist

print('Encoding started')

encodeknownlist = readencodings(imglist)
encodeknownlistwithids = [encodeknownlist, studentids]
print('Encoding complete')

#saving in a pickle file
file = open('Encodefile.p', 'wb')
pickle.dump(encodeknownlistwithids, file)
file.close()
print('file saved')