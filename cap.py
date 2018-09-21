import subprocess
import cv2
import pmail
#import time

def getpic():
    camera_port = 0
    cap = cv2.VideoCapture(camera_port)
    #time.sleep(0.1) for Mac
    print("Taking image...")
    ret, im = cap.read()
    if ret==True:
        file_name = "snap.jpg"
        cv2.imwrite(file_name, im)
    cap.release()

if __name__ == "__main__":
    getpic()
    pmail.setMail()