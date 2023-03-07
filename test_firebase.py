from say import say
from firebase import firebase
import time

firebase = firebase.FirebaseApplication('https://terralibrary-a9249-default-rtdb.firebaseio.com', None)

#result = firebase.get('/scans', { "orderBy": "code" })
result = firebase.get('/', "scans", params={ 'orderBy': "timestamp" })
#result = firebase.get('/scans', None)

print(result)
