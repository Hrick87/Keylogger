#libraries needed to host an http server
import http.server
import socketserver
import socket

def get_ip():
    #creates socket with TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # doesn't even have to be reachable, but will grab server's private ip
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        #in case the function fails, gives you loop back IP
        IP = '127.0.0.1'
    finally:
        #close socket
        s.close()
    return IP

#private ip of server stored in localIP
localIP = get_ip()

PORT = 8000

#handler configuration for basic HTTP server
Handler = http.server.SimpleHTTPRequestHandler

#creates HTTP server and hosts it on server's private IP and PORT
#Prints are for debugging, remove on final release
with socketserver.TCPServer((localIP, PORT), Handler) as httpd:
    print("serving at port", PORT)
    print(localIP)
    
    #keeps http server up until keylogging script is terminated with control-C
    httpd.serve_forever()
