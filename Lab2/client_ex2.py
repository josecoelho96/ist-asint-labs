import socket
s = socket.socket()
host = socket.gethostname()
port = 12345
s.connect((host, port))

valid_operations = ['sum', 'sub', 'push', 'pop']
operation = raw_input("Operation [sum, sub, push, pop]: ")

if operation in valid_operations:
    s.send(operation)
else:
    print 'Wrong operation'

#if operation in ['sum']

s.close