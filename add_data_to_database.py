import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':'https://faceattendance-f663d-default-rtdb.firebaseio.com/'
})

ref = db.reference('students')

data = {
    '280424':
        {
            'name':'Meerthika',
            'major':'Coding',
            'starting_year': '2023',
            'total_attendance': 10,
            'standing': 'G',
            'year':1,
            'last_attendance_time':'2024-05-01 00:54:34'
        },
    '290424':
            {
                'name':'Elon Musk',
                'major':'Economics',
                'starting_year': '2008',
                'total_attendance': 12,
                'standing': 'H',
                'year':16,
                'last_attendance_time':'2024-05-01 00:54:34'
            },
    '300424':
            {
                'name':'Mark Zuckerberg',
                'major':'Coding',
                'starting_year': '2004',
                'total_attendance': 12,
                'standing': 'P',
                'year':20,
                'last_attendance_time':'2024-05-01 00:54:34'
            }
}

for key,value in data.items():
    ref.child(key).set(value)