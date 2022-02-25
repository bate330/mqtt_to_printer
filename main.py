import sys, socket, time

import paho.mqtt.subscribe as subscribe
from SerialCom import SerialCom
from UdpCom import UdpCom


class Main:
    def __init__(self):
        self.host = 'broker.hivemq.com'
        self.topic = '/test'
        self.serialCom = SerialCom()
        self.msg = {bytes}
        # RS-232
        self.port = '/dev/ttyUSB0'
        self.baud = 9600
        # TCP
        self.ip = '192.168.0.22'
        self.udp_port = 3000

    def __on_message_print_special_channel(self, client, username, message):
        msg = message.payload.decode('utf-8')
        msg = msg.encode('ascii', 'ignore')
        try:
            SerialCom.rs_sender(self.port, self.baud, msg)
        except:
            print('no connection with printer')

    def __on_message_print_edgraf(self, client, username, message):
        msg = message.payload.decode('utf-8')
        msg = msg.encode('ascii', 'ignore')
        udpCom = UdpCom(self.ip, self.udp_port, msg)
        #try:
            # SerialCom.rs_sender(self.port, self.baud, msg)
        udpCom.udp_sender()
            #UdpCom.udp_receiver(self.ip, self.udp_port)
        #except:
        #    print('no connection with printer')

    def subscribe(self):
        try:
            subscribe.callback(callback=self.__on_message_print_edgraf, topics=self.topic, hostname=self.host)
        except socket.gaierror:
            print('no connection with broker')
        except KeyboardInterrupt:
            sys.exit()


project = Main()

while 1:
    project.subscribe()
    time.sleep(0)
