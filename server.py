import socket
import os
import signal
# device's IP address
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 51001
# receive 4096 bytes each time
BUFFER_SIZE = 4096

# create the server socket
# TCP socket
s = socket.socket()
# bind the socket to our local address
s.bind((SERVER_HOST, SERVER_PORT))
# enabling our server to accept connections
# 5 here is the number of unaccepted connections that
# the system will allow before refusing new connections
s.listen(5)
print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")
# accept connection if there is any
client_socket, address = s.accept() 
# if below code is executed, that means the sender is connected
print(f"[+] {address} is connected.\n")

# receive the file infos
# receive using client socket, not server socket
def handler(signum, frame):
    s.close()
    print("closed server socket\n")
    exit(0)

while True:
    signal.signal(signal.SIGINT, handler)
       
    while True:
        received = client_socket.recv(BUFFER_SIZE).decode()
        if "txt" in received:
            print("recieved: ", received, "\n")
            break
        elif received == '':
            print("recieved is empty: ", received, "\n")
            client_socket.close()
            print("closed client_socket connection\n")
            s.listen(5)
            print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")
            # accept connection if there is any
            client_socket, address = s.accept() 
            # if below code is executed, that means the sender is connected
            print(f"[+] {address} is connected.\n")
     
    # remove absolute path if there is
    filename = os.path.basename(received)
    print("removed absolute filepath of file\n")
    # start receiving the file from the socket
    # and writing to the file stream
    with open(filename, "wb") as f:
        while True:
            # read 1024 bytes from the socket (receive)
            bytes_read = client_socket.recv(BUFFER_SIZE)
            print("recieved ", bytes_read, " bytes.\n") 
            while bytes_read:
                # write to the file the bytes we just received
                f.write(bytes_read)
                print("wrote bytes into file\n")
                if "\n" in bytes_read.decode():
                    break
                # update the progress bar
                bytes_read = client_socket.recv(BUFFER_SIZE)
                print("wrote ", bytes_read, " bytes.\n")
            
            print("Bytes should be empty here, bytes: ", bytes_read, "\n") 
            break      
    f.close()
    print("closed file\n")  
    received = ''            
    print("set recived to: ", received, "\n")
