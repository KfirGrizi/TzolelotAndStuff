
import socket

import consts


def recv_from_connection(conn):
    data = b''
    while True:
        new_data = conn.recv(1024)
        if not new_data:
            break
        data += new_data
    return data


class CommunicationPeer:
    def __init__(self):
        self.sock = None
        self.conn = None

    def __del__(self):
        if self.sock:
            self.sock.close()
        if self.conn:
            self.conn.close()

    def listen_for_peer(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((consts.Communication.SERVER_HOST, consts.Communication.PORT))
        self.sock.listen(1)
        self.conn, addr = self.sock.accept()

    def connect_to_peer(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))

    def recv(self) -> bytes:
        curr_conn = self.sock
        # if self.conn is None than this peer is the communication's client, not the server
        if self.conn:
            curr_conn = self.conn
        return recv_from_connection(curr_conn)


    def send(self, bytes_to_send: bytes) -> None:
        curr_conn = self.sock
        # if self.conn is None than this peer is the communication's client, not the server
        if self.conn:
            curr_conn = self.conn
        curr_conn.sendall(bytes_to_send)





"""
# SERVER #####################
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        data = recv_from_connection(conn)
        conn.sendall(data)
##############################

# CLIENT #####################
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    data = recv_from_connection(s)

print('Received', repr(data))
##############################
"""




