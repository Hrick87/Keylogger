# What is this?

This program is a malicious script that logs a victims keyboard entries, then sends the logs back to a dummy email created by the hacker. It takes advantage of most people's neglect to change their default router information.
Infiltration goes as follows:
1. Victim downloads malicious script and is tricked into running securityUpdate.py by the hacker using social engineering.
2. securityUpdate.py is a keylogger that generates text logs of the victims keyboard input.
3. securityUpdate.py then calls httpServer.py as a subprocess and launches a http web server on port 8000 of the victims computer in the same file directory as the log files.
4. portforward.py accesses a victims router configuration by first finding their private IP on the network, then changes the routers default password, and creates a port forward on port 8000. 
5. Then portforward.py finds that victims public ip address, logs into a predetermined gmail account created by the hacker, stores the private ip in the drafts, and finally logs the victim out. This gmail will be accessed by securityUpdate.py
6. client.py on the hacker's end logs in to gmail grabs the stored public ip address of the victim in the drafts, then uses the ip address and a -wget command to download all files hosted on victims http server at port 8000.

## How to use

To enable use, in client.py change "INSERT EMAIL HERE" and "INSERT EMAIL PASSWORD HERE" to the dummy email you have set up to recieve the logs. In securityUpdate.py match these in the fields "EMAIL_ADDRESS =" and "EMAIL_PASSWORD ="

