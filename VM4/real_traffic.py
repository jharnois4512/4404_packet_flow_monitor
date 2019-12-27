import subprocess
from multiprocessing import Process
import time

def httpsTraffic():
	result = subprocess.check_output(['curl', '--cacert', 'server.pem', '--location', 'https://192.168.1.2:443'])
	print(result)
	print('\n==============================================\n')

while(1):
	httpsTraffic()
	time.sleep(1)
#httpsTraffic()
