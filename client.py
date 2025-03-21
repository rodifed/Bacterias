import socket
import random
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
sock.connect(("localhost", 10000))

text = [
    "У Лукаморья дуб зеленый",
    "Златая цепь на дубе том",
    "И днем и ночью Кот Ученый",
    "Все ходит по цепи кругом"
        ]

while True:
    sock.send(random.choice(text).encode())
    time.sleep(1)