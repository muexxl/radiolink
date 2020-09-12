from  ..radiolink import *
import time


radio=RF24(22,0)
radio.begin()
radio.powerDown()
time.sleep(0.4)
radio.powerUp()
radio.setAddressWidth(4)
radio.setChannel(0x4c)
radio.setAutoAck(0)
send_address= 0xc3b2a1c8.to_bytes(4,'little')
recv_address= 0xc3b2a1c7.to_bytes(4,'little')

radio.openReadingPipe(0,recv_address)
radio.openWritingPipe(send_address)
radio.enableDynamicPayloads()
radio.printDetails()


def ping():

    timeout = 50 #ms
    while 1:
        radio.stopListening()
        time1=time.time()*1e3
        buf=int(time.time()*1e6 % 2**32).to_bytes(4,'little')
        success=radio.write(buf)
        radio.startListening()
        print (f"Writing was {success}")
        while( time.time()*1000 < time1 + timeout):
            if radio.available():
                len=radio.getDynamicPayloadSize()
                buf = b''
                buf = radio.read(len)
                print ("Got Response")
                print (len, buf)            
                break
        
        time.sleep(1)

def pong():
    
    radio.startListening()
    radio.printDetails()
    while 1:
        if radio.available():
            len=radio.getDynamicPayloadSize()
            buf = b''
            buf = radio.read(len)
            radio.stopListening()
            radio.write(buf[:])
            radio.startListening()
            print (len, buf)

pong()