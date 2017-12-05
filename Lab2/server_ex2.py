import socket
from rpnCalculator import rpnCalculator

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))
s.listen(5)

while True:
    calc1 = rpnCalculator()

    c, addr = s.accept()

    print c.recv(1024)
    c.close()