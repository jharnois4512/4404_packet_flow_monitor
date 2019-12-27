import os
import sys
import socket
from scapy.all import *
import requests



############################################

num_arr = []
def send_packets():
	#s= socket.socket()
	#s.connect(("192.168.1.2", 4444))
	string1 = 'GET / HTTP/1.1\r\nHost: 192.168.1.2\r\n\r\n'
	request = IP(dst='10.4.7.2')/TCP(dport=4443)/string1
	request.display()
	send(request)

os.system("rm instr.txt")
def send_covert():
	global num_arr
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print("Socket successfully created")
	port = 4443
	s.connect(('192.168.1.2', port))
	while(1):
		for c in num_arr:
			string_c = str(c)
			#string_c = 'GET / HTTP/1.1\r\nHost: 192.168.1.2:4443\r\nUser-Agent: curl/7.47.0\r\nAccept: */*\r\n\r\n'
			#print("before sendall")
			s.send(str.encode(string_c, 'iso-8859-1'))
			#print("after sendall")
			while(1):
				#print("before recv")
				data1 = s.recv(1024)
				print(repr(data1))
				#print("after recv")
				break
			#print("after while_not_recv")
			print(string_c)
		#print("*****************done****************")
		print('before')
		num_arr = []
		data2 = s.recv(1024)
		print(repr(data2))
		#s.sendall(str.encode("HTTP/1.0 200 OK\n Content-Type: text/html\n\r\n", 'iso-8859-1'))
		s.send(str.encode("Recieve", 'iso-8859-1'))
		print('after')
		print("recieved data2")
		try:
			f = open("instr.txt", "r")
			s.close()
		except:
			continue

def send_badly(bad_instr):
        global num_arr
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Socket successfully created")
        port = 4443
        s.connect(('192.168.1.2', port))
        s.send(str.encode(bad_instr, 'iso-8859-1'))
        num_arr = []
        data2 = s.recv(1024)
        print(repr(data2))
        s.close()

def ascii_to_int(ascii_str):
	for c in ascii_str:
		num = ord(c)
		num_arr.append(num)
		print(num)
	print(num_arr)
	send_covert()

#ascii_to_int("  uname -r  ")
send_badly("  uname -r  ")



#main()
