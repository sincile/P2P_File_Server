from _thread import *
import socket
import select
import sys
# import LibraryTest

host = '127.0.0.1'

def create_socket(portNumber):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
    print("Socket made")
    try:
        server.bind((host, portNumber))
    except socket.error:
        print("Error when binding")
        sys.exit()
    print("Socket bound")
    server.listen(10)
    print("Socket is listening on: ", portNumber)
    return server


def client_connection(connect):
    connect.send(("Hello from the server").encode('utf-8'))
    while True:
        data = connect.recv(1024)
        server_reply = "Client data: " + data.decode('utf-8')
        if not data:
            break
        print(server_reply.encode('utf-8'))
        connect.sendall(("Recieved: " + server_reply).encode('utf-8'))
    connect.send(("Goodbye from the server").encode('utf-8'))
    connect.close()


def main():
    connection_list = []
    for port in range(1024,65535):
          try:
              connection_list.append(create_socket(port))
          except Exception:
              pass

    while True:
        #Monitor all conenction ports for activity
        s_read, s_write, s_error = select.select(connection_list,[],[])

        #Accept all clients wanting to connect
        for sock in s_read:
            if(sock in connection_list):
                sockfd, addr = server_sock.accept()
                connection_list.append(sockfd)
                print('Client ', addr ,' connected')
            else:
                try:
                    #_thread stuff goes here
                    data = sock.recv(1024)
                    if data:
                        sock.send(("Recieved: " + data.decode('utf-8')).encode())
                except:
                    print("Error recieving from client ", addr)
                    sock.send("Error recieving from client ", addr)
                    sock.close()
                    connection_list.remove(sock)
                    continue

    #Close all the sockets
    for i in connection_list:
        try:
            connection_list[i].close()
        except Exception:
            pass
        # connect, addr = sock.accept()
        # print("Connected with " + addr[0] + ":" + str(addr[1]))
        # start_new_thread(client_connection, (conn,))


if __name__ == '__main__':
    main()
