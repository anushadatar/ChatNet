
import socket
import sys
import chatRoom

# Get my IP address
my_ip = socket.gethostbyname(socket.gethostname())
#my_ip = '127.0.0.1'

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = (my_ip, 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

# Initialize the chatroom object
room = chatRoom.ChatRoom()

while True:
    print >>sys.stderr, '\nwaiting to receive message'

    # Receive a packet of <data> from an external machine with IP <address>
    data, address = sock.recvfrom(4096)
    
    # Log that n bytes of data were received from a certain address
    print >>sys.stderr, 'received %s bytes from %s' % (len(data), address)
    #print >>sys.stderr, data
    
    # Create message object to hold the data
    msg = chatRoom.Message()

    # Deserialize the json string back into a msg
    msg.deserialize(data, address)
    msg.printMsg()

    # Add the message to the chat thread
    room.append(msg)

    # Update the users in the chat
    room.update(sock)
