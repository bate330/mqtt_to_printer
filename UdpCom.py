import socket

class UdpCom:
    @staticmethod
    def tcp_sender(ip, port, msg):
        client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        client_socket.sendto(msg, (ip, port))
        print(msg)
