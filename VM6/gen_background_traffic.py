import subprocess
from multiprocessing import Process
import time

def httpsTraffic():
	result = subprocess.check_output(['curl', '--cacert', 'server.pem', '--location', 'https://192.168.1.2:443'])
	print(result)
	print('\n==============================================\n')

#def send_attack_instruct():
#	result = subprocess.check_output(['curl', '--cacert', 'server3.pem', '--location', 'https://10.4.7.2:4443'])

def runParallel(threads):
	proc = []
	for fn in range(threads):
#		print(fn)
		p = Process(target=httpsTraffic)
		p.start()
		proc.append(p)
	for p in proc:
		p.join()
n = 1000
while(n > 0):
	runParallel(5000)
	print(n)
	n=n-1
#httpsTraffic()
