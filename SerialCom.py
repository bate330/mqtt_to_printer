import serial
import time


class SerialCom:
    @staticmethod
    def rs_sender(port, baud, msg):
        ser = serial.Serial(port=port, baudrate=baud, timeout=None, bytesize=serial.EIGHTBITS,
                            parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, xonxoff=False, rtscts=False,
                            write_timeout=None, dsrdtr=False, inter_byte_timeout=None, exclusive=None)
        clear_buffer = b'\x18'
        eof = b'\x0d'
        print(msg)
        # ser.write(clear_buffer)
        # time.sleep(1)
        ser.write(msg + eof)