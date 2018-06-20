# encoding=utf-8
import socket
HOST = '10.211.51.3'
PORT = 10087
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

conn, addr = s.accept()
print 'connection' , addr
while 1:
	data = conn.recv(1024)
	if not data:break
	print repr(data)
	conn.sendall(data.upper())
conn.close()
