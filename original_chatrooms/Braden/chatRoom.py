
import socket
import json
import sys

#=======================================================================================

class Message:

    # By default set text to empty string and ID to the current IP address
    def __init__(self, text="", ID="", IP=socket.gethostbyname(socket.gethostname())):
         self.text = text
         self.IP = IP
         self.ID = ID
         if self.ID == "":
             self.ID = IP

    # Text variable modifier
    def setText(self, text):
        self.text = text

    # ID variable modifier
    def setID(self, ID):
        self.ID = ID

    # Print the message as it would appear in the chatroom
    def printMsg(self):
        print(self.ID + ": " + self.text)

    # Encode the data as a string that can be transmitted...
    def serialize(self):
        dictform = { 
            'text' : self.text,
            'ID' : self.ID
            # It doesn't need to carry its own IP because
            # the server can identify this for us (makes
            # spoofing a hair more difficult)
            }

        return json.dumps(dictform)

    # Extract message properties from an encoded json
    # string and assign those properties to itself
    def deserialize(self, jsonstring, address):
        dictform = json.loads(jsonstring)
        self.text = dictform['text']
        self.ID = dictform['ID']

        # The address should be passed in by the server,
        # it is not a part of the json string
        self.IP = address


#=======================================================================================

class ChatRoom:

    # By default create an empty list to use as a chat log
    def __init__(self, log=[]):
        self.log=log
        self.IPs=[]

    # Append a new message (object) to the chat log
    def append(self, msg):
        # NOTE - this function should only be used with message objects!
        self.log.append(msg)

        if msg.IP not in self.IPs:
            self.IPs.append(msg.IP)

    # Serialize the last message and send to all users
    def update(self, sock):
        data = self.log[len(self.log)-1].serialize()
        for address in self.IPs:
            sent = sock.sendto(data, address)
            #print >>sys.stderr, 'sent %s bytes back to %s' % (sent, address)


    # Print the last n messages from the log.
    # Prints the entire log by default.
    def printMessages(self, n='all'):

        # Prevent an out of bounds error
        if (n=='all') or (n > len(self.log)):
            n = len(self.log)

        print("--------------------------------------------")

        for c in range(0, n):

            # Grab a message that many steps from the end of the log
            msg = self.log[len(self.log)-1-c]

            # Print the message
            msg.printMsg()

        print("--------------------------------------------")



#=======================================================================================