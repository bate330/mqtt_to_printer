import sys, socket, time

import paho.mqtt.subscribe as subscribe
from SerialCom import SerialCom
from UdpCom import UdpCom


class Main:
    def __init__(self):
        self.host = 'broker.hivemq.com'
        self.topic = '/test'
        self.serialCom = SerialCom()
        self.udpCom = UdpCom()
        self.msg = {bytes}
        # RS-232
        self.port = '/dev/ttyUSB0'
        self.baud = 9600
        # TCP
        self.ip = '169.254.53.33'
        self.tcp_port = 1111

    def __on_message_print(self, client, username, message):
        msg = message.payload.decode('utf-8')
        msg = msg.encode('ascii', 'ignore')
        try:
            # SerialCom.rs_sender(self.port, self.baud, msg)
            UdpCom.tcp_sender(self.ip, self.tcp_port, msg)
        except:
            print('no connection with printer')

    def subscribe(self):
        try:
            subscribe.callback(callback=self.__on_message_print, topics=self.topic, hostname=self.host)
        except socket.gaierror:
            print('no connection with broker')
        except KeyboardInterrupt:
            sys.exit()


project = Main()

while 1:
    project.subscribe()
    time.sleep(0)
