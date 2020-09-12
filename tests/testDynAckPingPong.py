from  ..radiolink import *
import time



radio.setAddressWidth(5)
radio.setChannel(100)


radio.printDetails()

def ping():
    
    data=b'0123456789ABCDEF'
    send_address= 0xf0f0f0f0d2.to_bytes(5,'little')
    recv_address= 0xF0F0F0F0E1.to_bytes(5,'little')
    radio.openReadingPipe(0,send_address)
    radio.openWritingPipe(send_address)
    radio.openReadingPipe(1,recv_address)
    radio.printDetails()
    radio.stopListening()

    counter = 0
    while 1:
        print("Trying to send..")
        if(radio.write(data)):
            print ("Success!")
            len = radio.available()
            buf = radio.read(len)
            print(len, buf)
            counter = (counter + 1) %32
        
        time.sleep(0.8)

def pong():
    send_address= 0xf0f0f0f0d2.to_bytes(5,'little')
    recv_address= 0xF0F0F0F0E1.to_bytes(5,'little')
    radio.openReadingPipe(0,send_address)
    radio.openWritingPipe(send_address)
    radio.openReadingPipe(1,recv_address)

    radio.printDetails()
    radio.startListening()
    while 1:
        len =radio.available()
        if len:
            buf = b''
            buf = radio.read(len)
            print (len, buf)
        print (len)
        time.sleep(1)

pong()