from  RF24 import *
from .radioconfig import *
from datetime import datetime

config = RadioConfig()
radio= RF24(22,0) 
receive_buffer= bytearray(0)

def init():
    global config
    global radio
    radio = RF24(config.CEPin, config.CSNPin)
    radio.begin()

    radio.setAddressWidth(4)
    radio.setAutoAck(1)
    radio.enableDynamicPayloads()
    radio.enableAckPayload()
    #radio.enableDynamicAck()
    radio.setChannel(config.channel)
    radio.setDataRate(RF24_2MBPS)
    radio.setPALevel(RF24_PA_MAX)
    radio.setRetries(4,2)
    radio.startListening()
    set_adresses()


def set_adresses():
    global radio
    global config
    radio.openReadingPipe(0, config.get_master_address())
    radio.openReadingPipe(1, config.get_master_address())
    radio.openWritingPipe(config.get_master_address())
    radio.startListening()

def open_reading_and_writing_pipe(address: bytes):
    global radio
    radio.openReadingPipe(0,address)
    radio.openWritingPipe(address)

def send_to_id(id: int, data:bytearray):
    global config
    address= config.get_address_from_id(id)
    open_reading_and_writing_pipe(address)
    radio.stopListening()
    return send(data)

def send(data: bytearray):
    global radio
    print("Sending now data")
    print(data)
    return radio.write(data)
    

def send_to_address(address: bytes, data:bytearray):
    open_reading_and_writing_pipe(address)
    return send(data)

def send_to_master(data:bytearray):
    global config
    set_address(config.get_master_address())
    send(data)



def check_radio():
    global radio
    global receive_buffer
    len = 0
    if radio.available():
        len = radio.getDynamicPayloadSize()
        receive_buffer.extend(radio.read(len))
    return len

def check_radio_and_print_result():
    global receive_buffer
    len = check_radio()
    if len:

        s=datetime.strftime(datetime.now(),"%H:%m:%S.%f")[:-3] + "  | "
        for b in receive_buffer:
            s +=f" {b:02x}"
        receive_buffer.clear()
        print (s)

init()