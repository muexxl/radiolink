# -*- coding: utf-8 -*-

import struct


class RadioConfig(object):
    def __init__(self):
        self.CEPin = 22
        self.CSNPin = 0
        self.channel = 0
        self.broadcastAddress = 0xc3b2a1c7.to_bytes(4,'little')
        self.id =0
        self.addressPrefix = 0xe7
        self.addressPostfix = 0xe3
        self.channel = 0x64 #CH100 decimal
    
    def get_address_from_id(self, id):
        address = bytearray(4)
        address[0]=self.addressPrefix
        address[1:3]=struct.pack('<H',id)
        address[3] = self.addressPostfix
        return (bytes(address))

    def get_id_from_address(self, address: bytes):
        id_bytes = address[1:3]
        id = struct.unpack('<H',id_bytes)[0]
        return id

    def get_own_address(self):
        return get_address_from_id(self.id)
    
    def get_master_address(self):
        address_as_integer = int.from_bytes(self.broadcastAddress,'little')
        address_as_integer +=1
        return address_as_integer.to_bytes(4,'little')
    
    def get_broadcast_address(self):
        return self.broadcastAddress
