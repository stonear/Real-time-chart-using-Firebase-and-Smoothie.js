import time
from random import randint
import pyrebase

config = {
    "apiKey": "AIzaSyA88V9rTa-pQVvKR4tJckJ7GHtNH9uEdEY",
    "authDomain": "chart-b92ce.firebaseapp.com",
    "databaseURL": "https://chart-b92ce.firebaseio.com",
    "projectId": "chart-b92ce",
    "storageBucket": "chart-b92ce.appspot.com",
    "messagingSenderId": "203145862827"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
db.child("data").remove()

fixed_interval = 1 # dalam detik
while True:
    try:
        #temperature value obtained from Arduino + LM35 Temp Sensor
        nilai = randint(0, 9)

        #current time and date
        time_hhmmss = time.strftime('%H:%M:%S')
        date_mmddyyyy = time.strftime('%Y-%m-%d')

        #insert record
        data = {'date':date_mmddyyyy, 'time':time_hhmmss, 'value': nilai}
        db.child("data").push(data)
        print(data)

        time.sleep(fixed_interval)
    except IOError:
        print('Error! Something went wrong.')
