
import chatRoom
import json

msg = chatRoom.Message("Test message")
msg.printMsg()

jsonform = msg.serialize()
print(jsonform)

#dictform = json.loads(jsonform)
#print(dictform['ID'])

msg2 = chatRoom.Message()
msg2.deserialize(jsonform, '127.0.0.1')

msg2.printMsg()