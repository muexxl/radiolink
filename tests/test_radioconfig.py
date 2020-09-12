# -*- coding: utf-8 -*-

from .context import radiolink

import unittest

config =radiolink.RadioConfig()

class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_get_address(self):
        config.CEPin = 22
        config.CSNPin = 0
        assert config.channel == 0x64
        assert config.CEPin == 22
        assert config.get_address_from_id(0xeeff) == b'\xe3\xff\xee\xe7'
        assert config.get_id_from_address(b'\xe3\xff\xee\xe7') == 0xeeff
    
    def test_broadcast_address():
        assert config.broadcastAddress == b'\xc7\xa1\xb2\xc3'
        assert config.get_broadcast_address() ==  b'\xc7\xa1\xb2\xc3'

    def test_master_address(self):
        assert config.get_master_address() == b'\xc8\xa1\xb2\xc3'

if __name__ == '__main__':
    unittest.main()