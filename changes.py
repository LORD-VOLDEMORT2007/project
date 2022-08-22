import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/HP/Downloads"

class Files(FileSystemEventHandler):
    def on_created(self, event):
        print("file has been created")
    def on_deleted(self, event):
        print("file was deleted")
    def on_modified(self, event):
        print("file got modified")
    def on_moved(self, event):
        print("file got moved")

object =   Files()
obs = Observer()
obs.schedule(object , from_dir , recursive= True)

obs.start();

try:
    while True:
        time.sleep(2)
        print("running...")

except KeyboardInterrupt:
    print('stopped') 
    obs.stop()   