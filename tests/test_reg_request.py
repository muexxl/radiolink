from  ..radiolink import *
import time


radio=RF24(22,0)
radio.begin()
radio.powerDown()
time.sleep(0.4)
radio.powerUp()
radio.setAddressWidth(4)
radio.setAutoAck(1)
master_address= config.get_master_address()
recv_address= 0xc3b2a1c7.to_bytes(4,'little')

radio.openReadingPipe(0,master_address)
radio.openWritingPipe(master_address)
radio.enableDynamicPayloads()
radio.enableAckPayload()
#radio.enableDynamicAck()
radio.setChannel(100)
radio.setDataRate(RF24_2MBPS)
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