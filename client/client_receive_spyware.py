import socket
import os

HOST = "127.0.0.1"
PORT = 5555
BUFFER_SIZE = 4096 
SPLITOR = "<split>"


# create the client socket
s = socket.socket()
print("Connecting to :", PORT)
s.connect((HOST, PORT))
print("Successfully Connected.")
# Get the filename that exists
while True:
    exists = s.recv(16).decode()
    if exists != '0':
        received_filename = s.recv(BUFFER_SIZE).decode()
        filename, filesize = received_filename.split(SPLITOR)
        # Extract only filename
        filename = os.path.basename(filename)
        # convert filesize to integer
        filesize = int(filesize)
        # start receiving the file  
        with open(filename, "wb") as f:
            while (filesize):
                bytes_read = s.recv(BUFFER_SIZE)
                if not bytes_read:    
                    break
                f.write(bytes_read)
                filesize -= len(bytes_read)
        f.close()
        print("File stored :",filename)
    ans = s.recv(2).decode()
    if ans == 'y': 
        continue
    else: 
        break
# close the socket
s.close()
