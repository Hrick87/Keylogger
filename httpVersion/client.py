from subprocess import Popen
import urllib.request

def getPublicIP():
    PORT = '8000'
    external_ip = urllib.request.urlopen('https://api.ipify.org/').read().decode('utf8')

    return external_ip+':'+PORT

PUBLIC_IP = getPublicIP()
print(PUBLIC_IP) 
Popen('wget -r {PUBLIC_IP}', shell=True)