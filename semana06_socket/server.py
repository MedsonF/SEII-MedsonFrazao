import socket
import threading

HEADER = 64
PORT = 5050
SERVER  ="127.0.1.1"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client (conn, addr):
    print(f"[NEW CONNECTIONS] {addr} connected. ")

    connected = True 
    while connected:
        msg = conn.recv()


def start ():
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target = handle_client, args = (conn, args))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activateCount() - 1}")


        
print("[STARTING] server is starting...")   
start()