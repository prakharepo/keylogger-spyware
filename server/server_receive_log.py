import socket
import os

HOST = ""
PORT = 5555
BUFFER_SIZE = 4096
SPLITOR = "<split>"
# create the server socket (TCP)
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# bind the socket to address
s.bind((HOST, PORT))
s.listen(5)
print("Server is Listening on :", PORT)
client, address = s.accept() 

print('Connected to :', address[0], ':', address[1])

# receiving file using client socket
while True:
    exists = client.recv(16).decode()
    if exists != '0':
        received_filename = client.recv(BUFFER_SIZE).decode()
        filename, filesize = received_filename.split(SPLITOR)
        # Extract only filename
        filename = os.path.basename(filename)
        # convert filesize to integer
        filesize = int(filesize)
        # start receiving the file  
        with open(filename, "wb") as f:
            while (filesize):
                bytes_read = client.recv(BUFFER_SIZE)
                if not bytes_read:    
                    break
                f.write(bytes_read)
                filesize -= len(bytes_read)
        f.close()
        print("File stored :",filename)
    ans = client.recv(2).decode()
    if ans == 'y': 
        continue
    else: 
        break
# close client socket
client.close()
# close server socket
s.close()