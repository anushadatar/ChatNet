
import socket
import sys
import chatRoom

# Get my IP address
my_ip = socket.gethostbyname(socket.gethostname())
#my_ip = '127.0.0.1'

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = (my_ip, 10000)

my_ID = raw_input("Enter your name: ")

text = raw_input("> ")
msg = chatRoom.Message(text, ID=my_ID)

while text != "quit":

    

    try:
        # Send data
        packet = msg.serialize()
        sent = sock.sendto(packet, server_address)

        # Receive response
        data, server = sock.recvfrom(4096)

        # Create message object to hold the data
        msgBack = chatRoom.Message()

        # Deserialize the json string back into a msg
        msgBack.deserialize(data, server_address)
        msgBack.printMsg()

    finally:
        text = raw_input("> ")
        msg = chatRoom.Message(text, ID=my_ID)


print >>sys.stderr, 'closing socket'
sock.close()

