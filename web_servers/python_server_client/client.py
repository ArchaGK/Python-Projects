import socket
import sys

# Create a TCP/IP socket
from pip._vendor.distlib.compat import raw_input

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


port = 3333
IP = 'localhost'

# Connect the socket to the port where the server is listening
server_address = (IP, port)
print('starting up on ' + IP + ' port ' + str(port))
sock.connect(server_address)

try:

    # Send data
    message = b'This is the message.  It will be repeated.'
    print('sending {!r}'.format(message))
    sock.sendall(message)

    while True:

        data = sock.recv(1024)

        print('received ' + str(data.decode()))

        user_input = raw_input('enter command:')

        print(user_input)

        sock.sendall(user_input.encode())

        if user_input == 'quit':
            break




finally:
    print('closing client side socket')
    sock.close()