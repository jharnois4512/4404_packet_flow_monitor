import sys
import nfqueue
import socket
from scapy.all import *
from scapy.layers.inet import IP

num_arr = []
def ascii_to_int(ascii_str):
        for c in ascii_str:
                num = ord(c)
                num_arr.append(num)
                print(num)
        print(num_arr)
        send_packets()

#raw = 'GET / HTTP/1.1\r\nHost: 192.168.1.2:4443\r\nUser-Agent: curl/7.47.0\r\nAccept: */*\r\n\r\n'

def defense(i, p):
        print("working")
        data = p.get_data()
        pckt = IP(data)
        print(pckt[TCP].urgptr)
        ip = IP()
        tcp = TCP()
        raw = Raw()
        if (pckt.getlayer(Raw)):
                p.set_verdict(nfqueue.NF_DROP)
                pckt.show()
		try:
                        pckt[TCP].urgptr = int(pckt[Raw].load)
                except Exception, e:
			print("excepted")
                print(pckt[Raw].load)
                pckt.show2()
                print('/n/n/n')
                del pckt[IP].chksum
                del pckt[TCP].chksum
                #del pckt[IP].len
                #del pckt[TCP].dataofs
                #packet = pckt / raw_data
                pckt.show2()
                send(pckt)

q = nfqueue.queue()
q.open()
q.bind(socket.AF_INET)
q.set_callback(defense)
q.create_queue(5)
try:
        q.try_run()
except KeyboardInterrupt:
        q.unbind(socket.AF_INET)
        q.close()
