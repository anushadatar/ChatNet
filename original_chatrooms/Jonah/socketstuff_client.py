import socket
import sys


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 10001)
while True:
    message = input('Enter your message:\n')
    b_message = message.encode()

    try:
        print('sending "%s"' % message)
        sent = sock.sendto(b_message, server_address)

        print('waiting to receive')
        data, server = sock.recvfrom(4096)
        s_data = data.decode()
        print('from %s received:\n%s' % (server, s_data))

    finally:
        print('closing socket')
        sock.close
