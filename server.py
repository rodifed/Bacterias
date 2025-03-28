import socket
import time

main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
main_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
main_socket.bind(("localhost", 10000))
main_socket.setblocking(False)
main_socket.listen(5)
print("Socket init true")
players = []
while True:
    try:
        new_socket, addr = main_socket.accept()
        print(f"New player connected: {addr}")
        new_socket.setblocking(False)
        players.append(new_socket)
    except BlockingIOError as e:
        print("-")
    for sock in players:
        try:
            data = sock.recv(1024).decode()
            print(f"Received: {data}")
        except Exception as e:
            pass
    for sock in players:
        try:
            sock.send("Game".encode())
        except:
            players.remove(sock)
            sock.close()
            print("Socket closed")
    time.sleep(1)