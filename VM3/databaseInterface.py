import pymysql as db
import time

def check():
	mydb = db.connect("localhost", "root", "asdf1234", "snort")
	cursor = mydb.cursor()
	cursor.execute("""select count(*) from event where (select timestamp from event where sid = 0) - timestamp > 5;""")
	data = cursor.fetchone()
	mydb.close()
	return data

def updateNow():
	mydb = db.connect("localhost", "root", "asdf1234", "snort")
	cursor = mydb.cursor()
	cursor.execute("""update event set timestamp = now() where sid = 0;""")
	mydb.close()

def checkForFlood(data):
	if (data > 100):
		

while(1):
	updateNow()
	time.sleep(5)
	data = check()
	print(data)
	checkForFlood(data)	
