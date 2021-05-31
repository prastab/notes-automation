from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import json
import time
import datetime

now = datetime.datetime.now()
today = datetime.datetime.now().strftime("%A")
sunday = {
    "sub1": "Further", "sub1_teacher": "HSP", "sub1_start": now.replace(hour=8, minute=30), "sub1_end": now.replace(hour=9, minute=10),
    "sub2": "Maths", "sub2_teacher": "TA", "sub2_start": now.replace(hour=10, minute=40), "sub2_end": now.replace(hour=11, minute=20),
    "sub3": "Maths", "sub3_teacher": "AKC", "sub3_start": now.replace(hour=11, minute=30), "sub3_end": now.replace(hour=12, minute=10),
    "sub4": "Further", "sub4_teacher": "GMC", "sub4_start": now.replace(hour=12, minute=40), "sub4_end": now.replace(hour=13, minute=20),
    "sub5": "Physics", "sub5_teacher": "UA", "sub5_start": now.replace(hour=13, minute=30), "sub5_end": now.replace(hour=14, minute=10),
    "sub6": "Physics", "sub6_teacher": "HRT", "sub6_start": now.replace(hour=14, minute=20), "sub6_end": now.replace(hour=15, minute=00)}
monday = {
    "sub1": "Physics", "sub1_teacher": "VA", "sub1_start": now.replace(hour=8, minute=30), "sub1_end": now.replace(hour=9, minute=10),
    "sub2": "Maths", "sub2_teacher": "TA", "sub2_start": now.replace(hour=9, minute=20), "sub2_end": now.replace(hour=10, minute=00),
    "sub3": "Chemistry", "sub3_teacher": "RT", "sub3_start": now.replace(hour=10, minute=40), "sub3_end": now.replace(hour=11, minute=20),
    "sub4": "Chemistry", "sub4_teacher": "ShT", "sub4_start": now.replace(hour=11, minute=30), "sub4_end": now.replace(hour=12, minute=10),
    "sub5": "Further", "sub5_teacher": "LBR", "sub5_start": now.replace(hour=12, minute=40), "sub5_end": now.replace(hour=13, minute=20),
    "sub6": "Further", "sub5_teacher": "HSP", "sub6_start": now.replace(hour=13, minute=30), "sub6_end": now.replace(hour=14, minute=10)}
                                                          
tuesday = {
    "sub1": "Chemistry", "sub1_teacher": "UVK", "sub1_start": now.replace(hour=8, minute=30), "sub1_end": now.replace(hour=9, minute=10),
    "sub2": "Chemistry", "sub2_teacher": "MKJ", "sub2_start": now.replace(hour=9, minute=20), "sub2_end": now.replace(hour=10, minute=00),
    "sub3": "Maths", "sub3_teacher": "TKL", "sub3_start": now.replace(hour=10, minute=40), "sub3_end": now.replace(hour=11, minute=20),
    "sub4": "Maths", "sub4_teacher": "AKC", "sub4_start": now.replace(hour=11, minute=30), "sub4_end": now.replace(hour=12, minute=10),
    "sub5": "Further", "sub5_teacher": "GMC", "sub5_start": now.replace(hour=12, minute=40), "sub5_end": now.replace(hour=13, minute=20),
    "sub6": "English", "sub6_teacher": "GDJ", "sub6_start": now.replace(hour=13, minute=30), "sub6_end": now.replace(hour=14, minute=10),
    "sub7": "English", "sub7_teacher": "CD", "sub7_start": now.replace(hour=14, minute=20), "sub7_end": now.replace(hour=15, minute=00)}
wednesday = {
    "sub1": "Physics", "sub1_teacher": "HRT", "sub1_start": now.replace(hour=8, minute=30), "sub1_end": now.replace(hour=9, minute=10),
    "sub2": "Physics", "sub2_teacher": "VA", "sub2_start": now.replace(hour=9, minute=20), "sub2_end": now.replace(hour=10, minute=00),
    "sub3": "Maths", "sub3_teacher": "TA", "sub3_start": now.replace(hour=10, minute=40), "sub3_end": now.replace(hour=11, minute=20),
    "sub4": "Physics", "sub4_teacher": "UA", "sub4_start": now.replace(hour=11, minute=30), "sub4_end": now.replace(hour=12, minute=10),
    "sub5": "Further", "sub5_teacher": "HSP", "sub5_start": now.replace(hour=12, minute=40), "sub5_end": now.replace(hour=13, minute=20)}
thursday = {
    "sub1": "English", "sub1_teacher": "GDJ", "sub1_start": now.replace(hour=8, minute=30), "sub1_end": now.replace(hour=9, minute=10),
    "sub2": "English", "sub2_teacher": "CD", "sub2_start": now.replace(hour=9, minute=20), "sub2_end": now.replace(hour=10, minute=00),
    "sub3": "Maths", "sub3_teacher": "TA", "sub3_start": now.replace(hour=10, minute=40), "sub3_end": now.replace(hour=11, minute=20),
    "sub4": "Chemistry", "sub4_teacher": "UA", "sub4_start": now.replace(hour=11, minute=30), "sub4_end": now.replace(hour=12, minute=10),
    "sub5": "Chemistry", "sub5_teacher": "HSP", "sub5_start": now.replace(hour=12, minute=40), "sub5_end": now.replace(hour=13, minute=20),
    "sub6": "Further", "sub6_teacher": "LBR", "sub6_start": now.replace(hour=14, minute=20), "sub6_end": now.replace(hour=15, minute=00)}
friday = {
    "sub1": "Physics", "sub1_teacher": "UA", "sub1_start": now.replace(hour=8, minute=30), "sub1_end": now.replace(hour=9, minute=10),
    "sub2": "Physics", "sub2_teacher": "HRT", "sub2_start": now.replace(hour=9, minute=20), "sub2_end": now.replace(hour=10, minute=00),
    "sub3": "Chemistry", "sub3_teacher": "ShT", "sub3_start": now.replace(hour=10, minute=40), "sub3_end": now.replace(hour=11, minute=20),
    "sub4": "Chemistry", "sub4_teacher": "RT", "sub4_start": now.replace(hour=11, minute=30), "sub4_end": now.replace(hour=12, minute=10),
    "sub5": "Further", "sub5_teacher": "LBR", "sub5_start": now.replace(hour=12, minute=40), "sub5_end": now.replace(hour=13, minute=20),
    "sub6": "Further", "sub6_teacher": "HSP", "sub6_start": now.replace(hour=13, minute=30), "sub6_end": now.replace(hour=14, minute=10)}
friday = {


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + "/" + filename
            sub = ""
            teacher = ""
            now = datetime.datetime.now()
            if today == "Sunday":
                if sunday["sub1_start"] < now < sunday["sub1_end"]:
                    sub = sunday["sub1"]
                    teacher = sunday["sub1_teacher"]
                elif sunday["sub2_start"] < now < sunday["sub2_end"]:
                    sub = sunday["sub2"]
                    teacher = sunday["sub2_teacher"]
                elif sunday["sub3_start"] < now < sunday["sub3_end"]:
                    sub = sunday["sub3"]
                    teacher = sunday["sub3_teacher"]
                elif sunday["sub4_start"] < now < sunday["sub4_end"]:
                    sub = sunday["sub4"]
                    teacher = sunday["sub4_teacher"]
                elif sunday["sub5_start"] < now < sunday["sub5_end"]:
                    sub = sunday["sub5"]
                    teacher = sunday["sub5_teacher"]
                elif sunday["sub6_start"] < now < sunday["sub6_end"]:
                    sub = sunday["sub6"]
                    teacher = sunday["su6_teacher"]
            
            elif today == "Monday":
                if monday["sub1_start"] < now < monday["sub1_end"]:
                    sub = monday["sub1"]
                    teacher = monday["sub1_teacher"]
                elif monday["sub2_start"] < now < monday["sub2_end"]:
                    sub = monday["sub2"]
                    teacher = monday["sub2_teacher"]
                elif monday["sub3_start"] < now < monday["sub3_end"]:
                    sub = monday["sub3"]
                    teacher = monday["sub3_teacher"]      
                elif monday["sub4_start"] < now < monday["sub4_end"]:
                    sub = monday["sub4"]
                    teacher = monday["sub4_teacher"]
                elif monday["sub5_start"] < now < monday["sub5_end"]:
                    sub = monday["sub5"]
                    teacher = monday["sub5_teacher"]    
                elif monday["sub6_start"] < now < monday["sub6_end"]:
                    sub = monday["sub6"]
                    teacher = monday["su6_teacher"]

            elif today == "Tuesday":
                if tuesday["sub1_start"] < now < tuesday["sub1_end"]:
                    sub = tuesday["sub1"]
                    teacher = tuesday["sub1_teacher"]
                elif tuesday["sub2_start"] < now < tuesday["sub2_end"]:
                    sub = tuesday["sub2"]
                    teacher = tuesday["sub2_teacher"]
                elif tuesday["sub3_start"] < now < tuesday["sub3_end"]:
                    sub = tuesday["sub3"]
                    teacher = tuesday["sub3_teacher"]
                elif tuesday["sub4_start"] < now < tuesday["sub4_end"]:
                    sub = tuesday["sub4"]
                    teacher = tuesday["sub4_teacher"]
                elif tuesday["sub5_start"] < now < tuesday["sub5_end"]:
                    sub = tuesday["sub5"]
                    teacher = tuesday["sub5_teacher"]
                elif tuesday["sub6_start"] < now < tuesday["sub6_end"]:
                    sub = tuesday["sub6"]
                    teacher = tuesday["sub6_teacher"]
                elif tuesday["sub7_start"] < now < tuesday["sub7_end"]:
                    sub = tuesday["sub7"]
                    teacher = tuesday["sub7_teacher"]
    
    
            elif today == "Wednesday":
                if wednesday["sub1_start"] < now < wednesday["sub1_end"]:
                    sub = wednesday["sub1"]
                    teacher = wednesday["sub1_teacher"]
                elif wednesday["sub2_start"] < now < wednesday["sub2_end"]:
                    sub = wednesday["sub2"]
                    teacher = wednesday["sub2_teacher"]
                elif wednesday["sub3_start"] < now < wednesday["sub3_end"]:
                    sub = wednesday["sub3"]
                    teacher = wednesday["sub3_teacher"]
                elif wednesday["sub4_start"] < now < wednesday["sub4_end"]:
                    sub = wednesday["sub4"]
                    teacher = wednesday["sub4_teacher"]
                elif wednesday["sub5_start"] < now < wednesday["sub5_end"]:
                    sub = tuesday["sub5"]
                    teacher = tuesday["sub5_teacher"]
    
    
            elif today == "Thursday":
                if thursday["sub1_start"] < now < thursday["sub1_end"]:
                    sub = thursday["sub1"]
                    teacher = thursday["sub1_teacher"]
                elif thursday["sub2_start"] < now < thursday["sub2_end"]:
                    sub = thursday["sub2"]
                    teacher = thursday["sub2_teacher"]
                elif thursday["sub3_start"] < now < thursday["sub3_end"]:
                    sub = thursday["sub3"]
                    teacher = thursday["sub3_teacher"]
                elif thursday["sub4_start"] < now < thursday["sub4_end"]:
                    sub = thursday["sub4"]
                    teacher = thursday["sub4_teacher"]
                elif thursday["sub5_start"] < now < thursday["sub5_end"]:
                    sub = thursday["sub5"]
                    teacher = thursday["sub5_teacher"]
                elif thursday["sub6_start"] < now < thursday["sub6_end"]:
                    sub = thursday["sub6"]
                    teacher = thursday["sub6_teacher"]
    
    
            elif today == "Friday":
                if friday["sub1_start"] < now < friday["sub1_end"]:
                    sub = friday["sub1"]
                    teacher = friday["sub1_teacher"]
                elif friday["sub2_start"] < now < friday["sub2_end"]:
                    sub = friday["sub2"]
                    teacher = friday["sub2_teacher"]
                elif friday["sub3_start"] < now < friday["sub3_end"]:
                    sub = friday["sub3"]
                    teacher = friday["sub3_teacher"]
                elif friday["sub4_start"] < now < friday["sub4_end"]:
                    sub = friday["sub4"]
                    teacher = friday["sub4_teacher"]
                elif friday["sub5_start"] < now < friday["sub5_end"]:
                    sub = friday["sub5"]
                    teacher = friday["sub5_teacher"]
                elif friday["sub6_start"] < now < friday["sub6_end"]:
                    sub = friday["sub6"]
                    teacher = friday["sub6_teacher"]
            else:
                sub = "Screenshots"
                return sub, teacher

            if not os.path.isdir(folder_destination + "/" + sub + "/" + teacher + "/" + date):
                os.makedirs(folder_destination + "/" +
                            sub + "/" + teacher + "/" + date)
            else:
                print(folder_destination + " /" +
                      sub + "/" + teacher + "/" + date)
            new_destination = folder_destination + "/" + sub +\
                "/" + teacher + "/" + date + "/" + filename
            os.rename(src, new_destination)


today = datetime.datetime.now().strftime("%A")
date = datetime.datetime.today().strftime('%Y-%m-%d')
print(today, date)

folder_to_track = "/home/prastab/Pictures"
folder_destination = "/home/prastab/notes"

event_handler = MyHandler()
observer = Observer()

observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()
