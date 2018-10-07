import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
port = 3333
IP = 'localhost'
server_address = (IP, port)
print('starting up on ' + IP + ' port ' + str(port))


sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)


        while True:
            data = connection.recv(1024)
            print('received {!r}'.format(data))

            if data.decode() != 'quit':
                print('sending data back to the client')

                server_msg = b'server response'
                connection.sendall(server_msg)
            else:
                print('recieved quit command', client_address)
                break


    finally:
        # Clean up the connection
        print("Closing server side socket")
        connection.close()
        break
