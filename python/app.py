import threading
import time
from datetime import datetime
from random import randint
import json
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

class worker(threading.Thread):
   def __init__(self):
        threading.Thread.__init__(self)
        self.datas = []

   def run(self):
        while True:
            nilai = randint(0, 9)

            now = datetime.now()
            time_hhmmss = now.strftime('%H:%M:%S.%f')
            date_mmddyyyy = now.strftime('%Y-%m-%d')
            data = {'date':date_mmddyyyy, 'time':time_hhmmss, 'value': nilai}
            self.datas.append(data)

            time.sleep(0.005)

thread_serial = worker()

# Start new Threads
thread_serial.start()

fixed_interval = 1 # dalam detik
while True:
    try:
        datas = thread_serial.datas
        thread_serial.datas = []

        datas = json.dumps(datas)
        db.child("data").push(datas)
        print(datas)

        time.sleep(fixed_interval)
    except IOError:
        print('Error! Something went wrong.')
