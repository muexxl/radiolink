from  ..radiolink import *
import time


radio=RF24(22,0)
radio.begin()
radio.powerDown()
time.sleep(0.4)
radio.powerUp()
radio.setAddressWidth(4)
radio.setChannel(0x4c)
radio.setAutoAck(1)
send_address= 0xc3b2a1c8.to_bytes(4,'little')
recv_address= 0xc3b2a1c7.to_bytes(4,'little')

radio.openReadingPipe(0,recv_address)
radio.openWritingPipe(recv_address)
radio.enableDynamicPayloads()
radio.enableAckPayload()
#radio.enableDynamicAck()
radio.printDetails()


def pong():
    
    radio.startListening()
    radio.printDetails()
    while 1:
        if radio.available():
            len=radio.getDynamicPayloadSize()
            buf = b''
            buf = radio.read(len)
            radio.writeAckPayload(0,buf[:])
            print (len, buf)

pong()