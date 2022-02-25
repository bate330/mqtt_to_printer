import socket

class UdpCom:

    def __init__(self, ip, port, msg):
        self.ip = ip
        self.port = port
        self.msg = msg

    def udp_sender(self):
        stx = 2
        devno = 0
        frno = 1
        cb = 57
        eof = 13
        dlen = self.__calc_dlen(self.msg)
        chx = self.__calc_chx(devno, frno, cb, dlen, self.msg, eof)
        etx = 3
        frame = self.__get_frame(stx, devno, frno, dlen, cb, self.msg, eof, chx, etx)
        print(frame)
        client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        client_socket.sendto(frame, (self.ip, self.port))

    def __get_frame(self, stx, devno, frno, dlen, cb, msg, eof, chx, etx):
        return bytearray(bytes([stx]) + bytes([devno]) + bytes([frno]) + bytes([dlen]) + b'\x39' + msg + b'\x0d' + bytes([chx]) + bytes([etx]))

    def __calc_dlen(self, msg):
        return len(msg) + 2

    def __calc_chx(self, devno, frno, cb, dlen, msg, eof):
        sum = 0
        for byte in msg:
            sum += byte
        sum = sum + devno + frno + cb + dlen + eof
        result = 0 - sum
        print(result & 0xFF)
        return result & 0xFF

    @staticmethod
    def udp_receiver(ip, port):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_socket.bind((ip,port))
        data, addr = server_socket.recvfrom(1024)
        print("received msg: %s" % data)
