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
    filename = input("Enter filename :")
    # server should know send file not exists and wait for client response
    if not os.path.isfile(filename):
        client.send(('0').encode())
        print("File not exists")
    else:
        client.send(('1').encode())
        # Get file size
        filesize = os.path.getsize(filename)
        # Send name and size of file
        client.send(f"{filename}{SPLITOR}{filesize}".encode())
        # Sending the file
        with open(filename, "rb") as f:
            while (filesize):
                bytes_read = f.read(BUFFER_SIZE)
                if not bytes_read:
                    break
                client.sendall(bytes_read)
                filesize -= len(bytes_read)
        f.close()
    # Continue to send more files
    ans = input('\nDo you want to continue(y/n) :') 
    client.send(ans.encode())
    if ans == 'y': 
        continue
    else: 
        break
# close client socket
client.close()
# close server socket
s.close()