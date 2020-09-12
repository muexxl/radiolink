# python -m radiolink.tests.test_reg_request2

from  ..radiolink import *
import time

#open_reading_and_writing_pipe(config.get_address_from_id(0x0002))
radio.printDetails()
while 1:
    suc = send_to_id(2,bytearray(0xff04112233.to_bytes(5,'big')))
    print(f'Sending was {suc}')
    print("Received:")
    check_radio_and_print_result()
    time.sleep(0.5)
