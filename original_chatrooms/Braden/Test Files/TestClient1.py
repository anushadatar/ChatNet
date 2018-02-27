
# Sample code from
# https://pymotw.com/2/socket/udp.html#client-and-server-together

import socket
import sys

# Get my IP address
my_ip = socket.gethostbyname(socket.gethostname())
#my_ip = '127.0.0.1'

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = (my_ip, 10000)
message = 'This is the message.  It will be repeated.'

try:

    # Send data
    print >>sys.stderr, 'sending "%s"' % message
    sent = sock.sendto(message, server_address)

    # Receive response
    print >>sys.stderr, 'waiting to receive'
    data, server = sock.recvfrom(4096)
    print >>sys.stderr, 'received "%s"' % data

finally:
    print >>sys.stderr, 'closing socket'
    sock.close()
